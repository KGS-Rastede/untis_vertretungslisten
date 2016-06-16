function r(f){/in/.test(document.readyState)?setTimeout('r('+f+')',9):f()}

r(function(){
    var list = document.getElementById("mon_list").childNodes[1].childNodes;
    var bar = document.getElementById("bar");
    var perPageItems = 10;
    var allItems = list.length / 2;
    var page = 1;
    var itemsReaming = allItems;

    setInterval(function() {
      var items = perPageItems;
      if(itemsReaming - perPageItems <= perPageItems && itemsReaming > 0 && page > 1) {
        items = itemsReaming;
      } else if(itemsReaming <= 0) {
        page = 1;
        itemsReaming = allItems;
      }
      for (var i = 0; i < items; i++) {
        document.getElementById("mon_list").childNodes[1].appendChild(list[1]);
        document.getElementById("mon_list").childNodes[1].appendChild(list[2]);
        itemsReaming--;
      }
      var progress = ((allItems - itemsReaming) / allItems) * 100;
      bar.style.width = progress + "%";

      page++;
    }, 7000);
});
