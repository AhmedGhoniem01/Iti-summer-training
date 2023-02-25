print("counting number of vowels: ")
vowels=['a','e','i','o','u']
word=input("Enter word: ")
count=0
for x in word:
    if x in vowels:
        count+=1
print(f"The number of vowels is: {count}")
#--------------------------------------------------------------------------------------------
print("sorting array of 5 elements ascending and descending: ")
i=0
array=[]
while(i<5):
    num = int(input("Enter number: "))
    array.append(num)
    i+=1
array1=array.sort()
array2=array.sort(reverse=True)
print(f"array sorted ascending: {array1}")
print(f"array sorted descending:  {array2}")
#--------------------------------------------------------------------------------------------
count=0
print("printing number of times iti exsits in a string: ")
string=input("enter string: ")
list=string.split(" ")
str="iti"
for x in list:
    if(x == "iti"):
        count+=1
print(f"count of iti string in the list: {count}") 
    
# string=input("enter string: ")
# list=string.split(" ")
# str="iti"
# for x in list:
#     bool=True
#     if(len(x) == len(str)):
#         for i in range(0,len(str)):
#             if(x[i].lower() != str[i]):
#                 bool = False
#                 break
                
#         if(bool):
#             count+=1

# print(count)
#-------------------------------------------------------------------------------------------    
print("removing vowels from a word: ")
vowels = ['a','e','i','o','u']
word = input('enter string: ')
list =[]
for i in word:
    if i not in vowels:
        list.append(i)
print (f"string with vowels: {word}")
print(f"string without vowels: {list}")
#---------------------------------------------------------------------------------------------
print("viewing the locations of 'i' character: ")
string=input("Enter string: ")
list=[]
for x in string:
    if (x == "i"):
        list.append(string.index(x))
print(list)
#--------------------------------------------------------------------------------------------
print("Generate a multipication table: ")
num = int(input("Enter number: "))
x=1
y=1
array1=[]
array2=[]
while(x <= num):
    array1.append(x*y)
    if( x==y ):
        array2.append(array1)
        array1=[]
        x+=1
        y=1
    else:
        y+=1
print(array2)
#--------------------------------------------------------------------------------------------
print("building mario pyramid: ")
x=1
while( x<5 ):
    print(" " * (3-x))
    print("*" * (x))
    x+=1
#--------------------------------------------------------------------------------------------

