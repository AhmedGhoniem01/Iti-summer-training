//a- Get first anchor inside the second table then change its’ href property to training.com and it’s text to 'Training'
var a1 = document.getElementsByTagName("a")[0];
var tb2 = document.getElementsByTagName("table")[1];
a1.href = "http://www.training.com";
a1.text = "training";
var newRow = tb2.insertRow(3);
var newCell = newRow.insertCell(0);
newCell.append(a1);
//----------------------------------------------------------------------------------------------------------------------

//b- Find last image and change its borders to : solid pink 2px
var lastImg = document.getElementsByTagName("img")[1];
lastImg.style.border = "solid pink 2px" ;
//----------------------------------------------------------------------------------------------------------------------

//c- create Javascript function to Find all checkboxes (checked) in userData form and alert their values
function checked(){
    var checkBoxes = document.getElementsByName("hoppy");
    for (var i=0 ; i< checkBoxes.length ; i++){
        console.log(checkBoxes[i].checked);
        //alert(checkBoxes[i].checked);
    }
}
//----------------------------------------------------------------------------------------------------------------------

//d- Find element with id value “example” then change it’s background color to pink
var element = document.getElementById("example");
element.style.backgroundColor = "pink";