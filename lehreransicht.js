function r(f){/in/.test(document.readyState)?setTimeout('r('+f+')',9):f()}

r(function(){
    var list = document.getElementById("mon_list").childNodes[1].childNodes;
    var count = 2;

    console.log(list);

    setInterval(function() {
      for (var i = 0; i < 5; i++) {
        document.getElementById("mon_list").childNodes[1].appendChild(list[count]);
        document.getElementById("mon_list").childNodes[1].appendChild(list[count + 1]);
      }
    }, 2000);
});
