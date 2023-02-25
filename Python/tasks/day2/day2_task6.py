from random import randint as rand
words=["hangman","learning","information","evolution","maintainence"]
name = input("Enter your name to start the game: ")
word = words[rand(0,4)]
tries=10
guessed_word=list("_" * len(word))
victory = False
while(tries>0):
    char=input(f"Enter the next character to guess {name}: ")
    if char in word:
        for x in range(0,len(word)):
            if (word[x]==char):
                guessed_word[x]=char
        print(guessed_word)
        if(guessed_word == list(word)):
            victory=True
            break
    else:
        print("Character doesn't exist ")
    tries-=1
if(victory == True):
    print("you have won")
else:
    print("Game Over!")
    
print(guessed_word)