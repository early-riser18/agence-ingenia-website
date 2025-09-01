/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        blackPrimary: "var(--blackPrimary)",
        primary: "#4ab685",
        primaryDarker: "#41a377"

      },
      fontFamily :{
        'dm-sans': ['DM Sans', 'sans-serif'],
      },
    
    },
  },
  plugins: [],
}