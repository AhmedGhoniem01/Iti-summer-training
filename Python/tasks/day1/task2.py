from ctypes import Array


print("sorting array of 5 elements ascending and descending: ")
i=0
array=[]
while(i<5):
    num = int(input("Enter number: "))
    array.append(num)
    i+=1
array.sort()
print(f"array sorted ascending: {array}")
array.sort(reverse=True)
print(f"array sorted ascending: {array}")

