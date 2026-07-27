#!/usr/bin/env python3
"""
translate.py — AI documentation translation (Anthropic Claude version).

Usage:
  Translate changed files:  python translate.py -c content/en/
  Translate new files:      python translate.py -n content/en/
  Both:                     python translate.py -c -n content/en/
  Single file:               python translate.py content/en/guides/rate-limiting.md
  List only (test mode):    python translate.py -t -c content/en/
"""

import os
import sys
import re
import csv
import argparse
import subprocess
from pathlib import Path
from anthropic import Anthropic

# --- Configuration ---
SOURCE_LANG_DIR = "en"
TARGET_LANG_DIR = "ja"
TARGET_LANGUAGE = "Japanese"
MODEL = "claude-sonnet-5"
MAX_CHUNK_SIZE = 8192

PRESERVE_TERMS = ["API", "SDK", "OAuth", "webhook", "ID", "UUID", "REST", "JSON", "CLI"]
SKIP_DIRS = ["/misc", "/archive", "/drafts"]

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"], timeout=500)


# --- Change detection (git commit date comparison) ---

def get_last_commit_date(file_path):
    """Return epoch timestamp of the last commit touching this file."""
    result = subprocess.run(
        ["git", "log", "-1", "--format=%ct", file_path],
        capture_output=True, text=True
    )
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()
    return None


def is_source_newer(source_path, target_path):
    """True if source has a newer commit than target."""
    source_date = get_last_commit_date(source_path)
    target_date = get_last_commit_date(target_path)
    if source_date and target_date:
        return source_date >= target_date
    return True


def is_draft(file_path):
    """True if the file has draft: true in front matter."""
    result = subprocess.run(
        ["grep", "-q", "draft: true", file_path],
        capture_output=True, text=True
    )
    return result.returncode == 0


def get_files_to_translate(source_dir, new_files=False, changed_files=False):
    """Return list of source files that need translation."""
    files = []
    for root, dirs, filenames in os.walk(source_dir):
        if any(skip in root for skip in SKIP_DIRS):
            continue
        for filename in filenames:
            if not filename.endswith(".md"):
                continue
            source_path = os.path.join(root, filename).replace(os.sep, "/")
            target_path = source_path.replace(f"{SOURCE_LANG_DIR}/", f"{TARGET_LANG_DIR}/")
            target_exists = os.path.isfile(target_path)

            if is_draft(source_path):
                continue
            if not new_files and not changed_files:
                files.append(source_path)
                continue
            if changed_files and (not target_exists or is_source_newer(source_path, target_path)):
                files.append(source_path)
                continue
            if new_files and not target_exists:
                files.append(source_path)
    return files


# --- Chunking (split large files at heading boundaries) ---

def chunk_content(content):
    """Split content into chunks at heading boundaries."""
    chunks = []
    while len(content) > MAX_CHUNK_SIZE:
        last_heading = 0
        for match in re.finditer(r"\n#{2,5} ", content[:MAX_CHUNK_SIZE]):
            last_heading = match.start()
        last_newline = content[:MAX_CHUNK_SIZE].rfind("\n")
        split_point = last_heading if last_heading != 0 else last_newline
        if split_point <= 0:
            split_point = MAX_CHUNK_SIZE
        chunks.append(content[:split_point + 1])
        content = content[split_point:]
    chunks.append(content)
    return chunks


# --- Translation ---

def translate_chunk(chunk, target_language):
    """Translate one chunk of Markdown via the AI API."""
    preserve_note = ""
    if PRESERVE_TERMS:
        preserve_note = f"Do not translate these terms, keep them in English: {', '.join(PRESERVE_TERMS)}."

    system_message = f"""You are a technical documentation translator from English to {target_language}.
Rules:
1. Preserve all Markdown formatting exactly: headings, lists, code blocks, bold, italic, links.
2. Do not translate content inside code blocks (``` or `).
3. In front matter (between --- delimiters), only translate values for 'title', 'linktitle', and 'description'. Do not translate field names, slugs, dates, or other metadata.
4. Do not translate URLs, file paths, or shortcode syntax (content inside {{{{ }}}}).
5. {preserve_note}
6. Maintain the same line structure and paragraph breaks.
7. Produce accurate, natural {target_language} technical writing."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=8192,
        system=system_message,
        messages=[{"role": "user", "content": chunk}]
    )
    return next(block.text for block in response.content if block.type == "text")


def translate_file(source_path):
    """Translate a full file, chunking if needed."""
    with open(source_path, "r", encoding="utf-8") as f:
        content = f.read()
    chunks = chunk_content(content)
    translated = []
    for chunk in chunks:
        translated.append(translate_chunk(chunk, TARGET_LANGUAGE))
    return "\n".join(translated)


# --- Post-processing ---

def fix_internal_links(content, lang_prefix):
    """Add language prefix to internal Markdown links."""
    link_pattern = re.compile(r'\[(.*?)\]\((/[^)]*)\)')
    skip_extensions = ('.png', '.jpg', '.gif', '.jpeg', '.tgz', '.zip')

    def replace_link(match):
        text = match.group(1)
        url = match.group(2)
        if url.startswith(f"/{lang_prefix}") or url.endswith(skip_extensions):
            return match.group(0)
        return f"[{text}](/{lang_prefix}{url})"

    return link_pattern.sub(replace_link, content)


def apply_word_fixes(content, csv_path):
    """Apply terminology corrections from a word-fix CSV."""
    if not os.path.isfile(csv_path):
        return content
    with open(csv_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("dst_old") and row.get("dst_new"):
                content = content.replace(row["dst_old"], row["dst_new"])
    return content


# --- Main ---

def main():
    parser = argparse.ArgumentParser(description="Translate documentation.")
    parser.add_argument("source", help="Source file or directory")
    parser.add_argument("-n", "--new", action="store_true", help="Only new files")
    parser.add_argument("-c", "--changed", action="store_true", help="Only changed files")
    parser.add_argument("-t", "--test", action="store_true", help="List files only")
    args = parser.parse_args()
    args.source = args.source.replace(os.sep, "/")

    if f"{SOURCE_LANG_DIR}/" not in args.source:
        print(f"Source path must contain '{SOURCE_LANG_DIR}/'")
        sys.exit(1)

    if os.path.isfile(args.source):
        files = [args.source]
    elif os.path.isdir(args.source):
        files = get_files_to_translate(args.source, new_files=args.new, changed_files=args.changed)
    else:
        print("Source must be a file or directory")
        sys.exit(1)

    if not files:
        print("No files to translate.")
        sys.exit(0)

    print(f"Files to translate: {len(files)}")
    if args.test:
        for f in files:
            print(f"  {f}")
        sys.exit(0)

    # Word-fix CSV path (adjust for your repo)
    word_fix_csv = os.path.join(os.path.dirname(__file__), f"en-{TARGET_LANG_DIR}.csv")

    success = 0
    for source_path in files:
        print(f"  {source_path}")
        try:
            translated = translate_file(source_path)
            if translated:
                # Post-process
                translated = fix_internal_links(translated, TARGET_LANG_DIR)
                translated = apply_word_fixes(translated, word_fix_csv)

                # Write to target
                target_path = source_path.replace(f"{SOURCE_LANG_DIR}/", f"{TARGET_LANG_DIR}/")
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                with open(target_path, "w", encoding="utf-8") as f:
                    f.write(translated)
                success += 1
        except Exception as e:
            print(f"    Failed: {e}")

    print(f"\nTranslated: {success}/{len(files)}")


if __name__ == "__main__":
    main()
