print("viewing the locations of 'i' character: ")
string=input("Enter string: ")
list=[]

for i in range(0,len(string)):
    if (string[i] == "i"):
        list.append(i)
print(list)
