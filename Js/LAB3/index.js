var students = [{ fname: 'ali', age: 22, grade:100 },
       { fname: 'nora', age: 20, grade:90 },
       { fname: 'nada', age: 25, grade:75 },
       { fname: 'heba', age: 19, grade:50 },
       { fname: 'bassem', age: 21, grade:40 }
       ];
       
console.log("All Students: ");
document.write(' <h1 style="color: red;" >All Students: </h1> ');
students.forEach(function(element){
    console.log("Name: "+element.fname+" ,Age: "+element.age+" ,Grade: "+element.grade);
    document.write('<p> Name: '+element.fname+" ,Age: "+element.age+" ,Grade: " + element.grade + '</p>');
});
       
var greater = students.filter(function(element){
    return element.grade > 80;
});

var sorted = students.sort(function(a,b){
     if ( a.fname.toLowerCase() > b.fname.toLowerCase() )
     return 1;
     else if ( a.fname.toLowerCase() < b.fname.toLowerCase() )
     return -1;
     else
     return 0;
});

console.log("Students that have a grade larger than 80: ");
document.write(' <h1 style="color: red;" >Students that have a grade larger than 80: </h1> ');
greater.forEach(function(element){
    console.log("Name: "+element.fname+" ,Age: "+element.age+" ,Grade: "+element.grade);
    document.write('<p> Name: '+element.fname+" ,Age: "+element.age+" ,Grade: " + element.grade + '</p>');
});

console.log("Students sorted by name: ");
document.write(' <h1 style="color: red;">Students sorted by name: </h1> ');
sorted.forEach(function(element){
    console.log("Name: "+element.fname+" ,Age: "+element.age+" ,Grade: "+element.grade);
    document.write('<p> Name: '+element.fname+" ,Age: "+element.age+" ,Grade: " + element.grade + '</p>');

});