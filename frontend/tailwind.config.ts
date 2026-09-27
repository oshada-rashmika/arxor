import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          terracotta: '#D86B43',
          'terracotta-dark': '#BF532C',

          forest: '#24523B',
          'forest-light': '#4A7C61',

          cream: '#FAF9F6',

          charcoal: '#1C2421',
          muted: '#5E6E66',

          border: '#E8E6DF',

          gold: '#E09F3E',
        },
      },
    },
  },
  plugins: [],
};

export default config;