/** @type {import('tailwindcss').Config}*/
const defaultTheme = require('tailwindcss/defaultTheme');
module.exports = {
	content: [
		'./templates/**/*.html',
		'./*/templates/**/*.html',
		"./accounts/templates/**/*.html",
    	"./transcripts/templates/**/*.html",
	],
	theme: {
		extend: {
			fontFamily: {
			  sans: ['Inter var'],
			},
		  },
	},
	plugins: [],
}
