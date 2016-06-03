function animate(elem,style,from,to,time,prop) {
    if( !elem) return;
    var start = new Date().getTime(),
        timer = setInterval(function() {
            var step = Math.min(1,(new Date().getTime()-start)/time);
            if (prop) {
                elem[style] = (from+step*(to-from));
            } else {
                elem.style[style] = (from+step*(to-from));
            }
            if( step == 1) clearInterval(timer);
        },25);
    elem.style[style] = from;
}

window.onload = function () {
  animate(document.body, "scrollTop", 0, window.innerHeight, 33000, true);
};
