print("removing vowels from a word: ")
vowels = ['a','e','i','o','u']
word = input('enter string: ')
list =[]
brief=""
for i in word:
    if i not in vowels:
        brief+=i
print (f"string with vowels: {word}")
print(f"string without vowels: {brief}")