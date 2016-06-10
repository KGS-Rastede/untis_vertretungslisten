function r(f){/in/.test(document.readyState)?setTimeout('r('+f+')',9):f()}

r(function(){
    var list = document.getElementById("mon_list").childNodes[1].childNodes;
    var bar = document.getElementById("progress");
    var perPageItems = 10;
    var progress = (100 / (list.length / 2)) * perPageItems;
    var page = 1;
    var count = 2;

    setInterval(function() {
      for (var i = 0; i < perPageItems; i++) {
        document.getElementById("mon_list").childNodes[1].appendChild(list[count]);
        document.getElementById("mon_list").childNodes[1].appendChild(list[count + 1]);
      }
      page++;
      if(page >= (list.length / 2) / perPageItems) {
        bar.style.width = "0%";
        page = 1;
      }  else {
        bar.style.width = progress * page + "%";
      }
    }, 7000);
});
