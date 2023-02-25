var i=0;
setInterval(function(){
    document.write(' <p style=" border: red solid 2px; display: inline-block; " > '+ i + ' </p></br> ');
    document.title = i;
    i++;
} , 1000);

// function insert_Row(){
//     var x = document.getElementById("table").insertRow(0);
//     var y = x.insertCell(0);
//     y.innerHTML = i;
//     document.title = i
//     i++
// }
// setInterval(insert_Row,1000);
