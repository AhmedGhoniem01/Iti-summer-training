//All of these commands are taken from console//


//a- Find all images in page by two ways (document default collection and document methods
//First method:
var img1 = document.getElementsByTagName("img")[0];
var img2 = document.getElementsByTagName("img")[1];
//Second method:
// var img1 = document.getElementsByName("firstImg");
// var img1 = document.getElementById("secondImg");
//----------------------------------------------------------------------------------------

//b- Find all options for City drop down list
var city = document.getElementsByClassName("bPink");
//now city is an array containing all options as elements
//----------------------------------------------------------------------------------------

//c- Find all rows for second table in page
var rows =document.getElementsByTagName("table")[1];
//Iterating through the rows of the second table
// var i =0;
// rows.forEach(function(){
//     rows.getElementsByTagName("tr")[i];
//     i++;
// })
//---------------------------------------------------------------------------------------

// d- Find all elements that contain class name fontBlue
var elements = document.getElementsByClassName("fontBlue");
//Array of all elements of the class fontBlue
//---------------------------------------------------------------------------------------


