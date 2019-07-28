function once(a,c){var b;return function(){a&&(b=a.apply(c||this,arguments),a=null);return b}}var canOnlyFireOnce=once(function(){console.log("Fired!")});canOnlyFireOnce();canOnlyFireOnce();
