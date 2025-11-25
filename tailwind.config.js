/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'brand-bg': '#F9F9F7',       /* Off-white creme */
        'brand-text': '#4B3621',     /* Marrom Café Profundo */
        'brand-accent': '#DCAE96',   /* Dusty Rose */
        'brand-accent-hover': '#C69C85',
        'brand-secondary': '#B2AC88', /* Sálvia suave */
      },
      fontFamily: {
        serif: ['"Playfair Display"', 'serif'],
        sans: ['"Lato"', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
