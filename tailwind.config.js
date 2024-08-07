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
        gray1: "#222831",
        gray2: "#76ABAE",
        hover: "#00ADB5",
        page1: "#F4EEE0",
      },
      light: {
        white: "#EEEEEE",
        white2: "#D8D8D8",
        hover: '#CCCCCC',
        green: "#76ABAE",
        gray1: "#31363F",
        gray2: "#222831",
      }
    },
    extend: {},
  },
  plugins: [],
}

