function debounce(b,f,c){var a;return function(){var d=this,e=arguments,g=c&&!a;clearTimeout(a);a=setTimeout(function(){a=null;c||b.apply(d,e)},f);g&&b.apply(d,e)}}var myEfficientFn=debounce(function(){},250);window.addEventListener("resize",myEfficientFn);