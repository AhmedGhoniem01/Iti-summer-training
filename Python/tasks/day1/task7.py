print("building mario pyramid: ")
num = int(input("Enter the value of rows: "))
x=1
while( x <= num ):
    print(" " * (num-x))
    print("*" * (x))
    x+=1
    