/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
          boxShadow: {
            '4xl': '0 0 15px rgba(0, 0, 0, 0.1)',
            '5xl': '0 0 10px rgba(0, 0, 255, 0.3)',
            '6xl': '0 0 10px rgba(0, 0, 0, 0.2)',
            '7xl': '0 0 10px rgba(0, 0, 0, 0.1)',
            '8xl': '0 0 10px rgba(255, 255, 255, 0.3)',
            '9xl': '0 0 5px rgba(0, 0, 0, 0.1)',
            '10xl': '0 0 5px rgba(0, 0, 0, 0.25)',
          },
        },
  },
  plugins: [],
}

