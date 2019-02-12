var ListOfNodes = document.getElementsByTagName("LI");
 var i;
for (i = 0; i < ListOfNodes.length; i++) {
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    ListOfNodes[i].appendChild(span);
}

var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var curDiv = this.parentElement;
    curDiv.style.display = "none";
  }
}

var listOfItems = document.querySelector('ul');
listOfItems.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('done');
  }
}, false);

function newItemAdd() {
  var lists = document.createElement("li");
  var val = document.getElementById("inputID").value;
  var t = document.createTextNode(val);
  lists.appendChild(t);
  if (val === '') {
    alert("Type something!");
  } else {
    document.getElementById("ulist").appendChild(lists);
  }
  document.getElementById("inputID").value = "";
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("delete");
  span.className = "close";
  span.appendChild(txt);
  lists.appendChild(span);
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var curDiv = this.parentElement;
      curDiv.style.display = "none";
    }
  }
}