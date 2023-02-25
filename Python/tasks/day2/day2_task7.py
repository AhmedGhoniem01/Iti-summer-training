alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
temp = list(input("enter your string: ").lower())
list1=[]
list2=[]
total=0

for x in range(0 , len(temp)):
    index = alphabet.index(temp[x])
    count=0
    list1=[]
    list1.append(temp[x])
    for y in range(x+1 , len(temp)):
        if alphabet.index(temp[y]) > index:
            count+=1
            index = alphabet.index(temp[y])
            list1.append(temp[y])

    if count > total :
        total = count
        list2=list1
    

print("Largest common subsequence is: ")
print(list2)
