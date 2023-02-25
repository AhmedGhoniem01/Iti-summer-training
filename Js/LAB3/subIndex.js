var str = "welcome to js";
var i=0;

timerId = setInterval(function(){
    document.write(str[i]);
    i++;
    if(i == str.length){
        clearInterval(timerId);
    }

} , 1000);
