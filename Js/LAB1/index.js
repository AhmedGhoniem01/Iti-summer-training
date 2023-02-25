//--------------------------------------------------
// extract unique characters
var str1 = "thequickbrownfoxjumpsoverthelazydog";
console.log(str1);
var str2="" ;
for (let i=0 ; i<= str1.length ; i++){
    if(str1.indexOf(str1[i]) == i){
        str2 += str1[i];
    }
}
console.log(str2);

//--------------------------------------------------
// find longest word
var str = 'Web Development Tutorial';
list = str.split(" ");
var max = list[0].length;
var word = list[0];
for (let i=1 ; i< list.length ; i++){
    if(list[i].length > max){
        max = list[i].length;
        word=list[i];
    }
}
console.log(word);

//--------------------------------------------------
