addEventListener("load" , function(){
    var btn = document.getElementById("btn")[0];
    
    btn.addEventListener("click" , function(){
        var color1 = (Math.random() * 0xFFFFFF << 0).toString(16);
        var color2 = (Math.random() * 0xFFFFFF << 0).toString(16);
        document.body.style.backgroundColor = "linear-gradient(to right,"+color1+","+color2+")";    
    });

});