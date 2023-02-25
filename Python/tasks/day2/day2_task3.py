def reversed(str):
    str2=""
    for i in range(len(str)-1,-1,-1):
        str2+=str[i]
    return str2

str = input("Enter string: ")
print(reversed(str))