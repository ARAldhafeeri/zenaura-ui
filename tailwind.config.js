/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'selector',
  content: [
    './public/index.html', "./public/**/*.py"
  ],
  theme: {
    colors: {
      dark: {
        black: "#040D12",
        purble1: "#393646",
        gray1: "#393646",
        page1: "#F4EEE0",
      },
      light: {
        white: "#EEEEEE",
        green: "#76ABAE",
        gray1: "#31363F",
        gray2: "#222831",
      }
    },
    extend: {},
  },
  plugins: [],
}

