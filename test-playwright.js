const { chromium } = require('playwright');

(async () => {
  console.log('Launching browser...');
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();
  
  console.log('Navigating to your docs...');
  await page.goto('https://task-manager-api-documentation.vercel.app/');
  
  console.log('Taking screenshot...');
  await page.screenshot({ path: 'test-screenshot.png' });
  
  console.log('Success! Check test-screenshot.png');
  await browser.close();
})();