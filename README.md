# Purple CSS Converter

Simple Python script that walks a path and for each CSS file checks for instances of a few URLs and replaces them with other URLs

I made this to aid in my self hosted version of [Gilbn's Theme Park](https://github.com/gilbN/theme.park). These are CSS themes for various webUI services that you can inject into the page at the reverse proxy stage of the request. Dark mode everywhere! Intead of using the regular CSS files from Gilbn (hosted on github so an external call is required every page load) I'm hosting them on my Nginx server itself. The scripts have URL references to eachother and references so this script basically just points those URLs to the local versions.