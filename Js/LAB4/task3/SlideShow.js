addEventListener("load", function () {

   imjobj = document.getElementsByTagName("img")[0];
   next = document.getElementsByClassName("gg-arrow-right-r")[0];
   prev = document.getElementsByClassName("gg-arrow-left-r")[0];
   Startobj = document.getElementsByClassName("gg-play-stop-o")[0];
   stopobj = document.getElementsByClassName("gg-play-button-o")[0];

    counter = 1;
    next.addEventListener("click", function () {
        counter++;
        if (counter == 5)
            counter = 1;
        imjobj.src = "images/" + counter + ".jpg";
    })// next

    prev.addEventListener("click", function () {
        counter--;
        if (counter == 0)
            counter = 4;
        imjobj.src = "images/" + counter + ".jpg";
    })// prev

    startobj.addEventListener("click" , function(){
        timer_id = setInterval(function (){
        counter++;
        if (counter == 5)
            counter = 1;
        imjobj.src = "images/" + counter + ".jpg";
        } , 1000);
    })//play

    stopobj.addEventListener("click" , function(){
        clearInterval(timer_id);
    })//pause

})// load 