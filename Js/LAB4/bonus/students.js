addEventListener("load" , function(){
    var _name = document.getElementById("nameTxt");
    var _age = document.getElementById("ageTxt");
    var _grade = document.getElementById("gradeTxt");
    var _dept = document.getElementById("deptVal");
    var _btn = document.getElementById("btn");
    var table = document.getElementById("stdTable");
    
    var row_counter=0 ;
    var newRow ;
    var newCell; 

    _btn.addEventListener("click" , function(){
        var values = [_name.value , _age.value, _grade.value, _dept.value];
        newRow  = table.insertRow(row_counter);
        for(var i=0 ; i<=3 ; i++){
            newCell = newRow.insertCell(i);
            newCell.append(values[i]);
        }
        row_counter++;
    })

});