/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./test.html",
    "./test_static.html",
    "use_case1_questions.html",
    "./src/**/*.{js,ts,jsx,tsx,html}",
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