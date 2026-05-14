const fs = require('fs');
fs.cpSync('ref_repo/app-base-fullstack-main/backend', 'backend', { recursive: true });
fs.cpSync('ref_repo/app-base-fullstack-main/fontend', 'frontend', { recursive: true });
