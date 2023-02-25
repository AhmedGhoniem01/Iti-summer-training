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