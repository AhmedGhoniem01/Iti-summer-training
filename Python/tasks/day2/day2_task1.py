def make_array(len,start):
    array=[]
    for i in range(start,(start+len+1)):
        array.append(start)
        start+=1
    return array
len = int(input("Enter the length of the array: "))
start = int(input("Enter the value of the first element: "))
array = make_array(len,start)
print(array)
