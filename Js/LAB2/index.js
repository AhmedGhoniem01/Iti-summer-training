var arr = [1,5,10,4,50,60,3,70,1,5,100,10];
console.log(arr);
var arr2 = [];
for (var i=0 ; i<arr.length ; i++){
    if (arr.indexOf(arr[i]) == i){
        arr2.push(arr[i]);
    }
}
console.log("Removing duplicate elements: ")
console.log(arr2);
//-----------------------------------------------------------
arr2.sort(function(a,b){
    return a-b;
});
console.log("Sorting the array elements: ")
console.log(arr2);
//----------------------------------------------------------
// var arr3 = []
// arr2.forEach(function(a,b){
//     if (a>50){
//         arr3.push(a);
//     }
// });
// console.log("Numbers larger than 50: ")
// console.log(arr3);

arr3 = arr2.filter(function(a){
    return a>50;
});
console.log("Numbers larger than 50: ")
console.log(arr3);
//----------------------------------------------------------
var max = arr2[0];
var min = arr2[0];
arr2.forEach(function(a,b){
    if (a> max){
        max = a;
        }
    if (a<min){
        min = a;
    }
});
console.log("Max and Min number: ")
console.log("max= "+max+" ,min= "+min);

console.log("Max and Min number using ES6 Math functions: ")
var max2 = arr2.reduce((a, b) => Math.max(a, b));
var min2 = arr2.reduce((a, b) => Math.min(a, b));
console.log("max= "+max2+" ,min= "+min2);

//-------------------------------------------------------------------------------
function sumAll(arr){
    return eval(arr.join("+"));
}

function multAll(arr){
    return eval(arr.join("*"));
}

var arr = [1,8,6,10];
console.log("Array numbers summation: ");
console.log(sumAll(arr));
console.log("Array numbers multipication: ");
console.log(multAll(arr));
//------------------------------------------------------------------------------