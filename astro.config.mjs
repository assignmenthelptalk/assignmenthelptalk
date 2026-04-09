import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://assignmenthelptalk.com',
  trailingSlash: 'ignore',
  integrations: [
    tailwind(),
  ],
  output: 'static',
});
