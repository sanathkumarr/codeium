/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}", // Scan all JS/TS/JSX/TSX files in src folder
    "./public/index.html"         // Also include your HTML entry point
  ],
  theme: {
    extend: {
      // You can extend colors, fonts, spacing, etc. here if needed
    },
  },
  plugins: [],
};
