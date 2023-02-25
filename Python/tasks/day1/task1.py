print("counting number of vowels: ")
vowels=['a','e','i','o','u']
word=input("Enter word: ")
count=0
for x in word:
    if x in vowels:
        count+=1
print(f"The number of vowels is: {count}")