import React from 'react';
import styles from './styles.module.css';

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container text--center padding-vert--xl">
        <h1>Welcome to the Task Manager API Docs</h1>
        <p>
          Explore the API reference, test endpoints, and view responses in real time 
          using our interactive <strong>Live API Console</strong>.
        </p>
      </div>
    </section>
  );
}