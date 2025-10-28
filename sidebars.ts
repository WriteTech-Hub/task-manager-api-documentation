import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docsSidebar: [
    // 'intro',
    // {
    //   type: 'category',
    //   label: 'Setup',
    //   items: [
    //     'setup/installation',
    //     'setup/env',
    //   ],
    // },
    {
      type: 'category',
      label: 'API Reference',
      items: [
        'api/authentication',
        'api/tasks',
        'api/users',
      ],
    },
    // {
    //   type: 'category',
    //   label: 'UI Guide',
    //   items: [
    //     'ui/how-it-maps-to-api',
    //   ],
    // },
  ],
};

export default sidebars;