count=0
print("printing number of times iti exsits in a string: ")
string=input("enter string: ")
list=string.split(" ")
str="iti"
for x in list:
    if(x == "iti"):
        count+=1
print(f"count of iti string in the list: {count}") 