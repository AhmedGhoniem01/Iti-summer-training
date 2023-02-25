var ref = open("sub.html" , "child" , "width=300 , height=300");
var str = "welcome to js";

setTimeout( function() {
    ref.close();
} , Number(str.length + 1)*1000); 
