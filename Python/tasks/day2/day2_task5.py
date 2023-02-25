num=input("Enter a number: ")
total=0
count=0
while(num.lower() != "done"):
    if not (num.isdigit()):
        # raise Exception("you must enter a number or enter 'done' ")
        print("You must enter a number or enter 'done' ")
    else:
        total+=int(num)
        count+=1
    num=input("Enter a number: ")
print(f"Count: {count}, Total: {total}, Average: {total/count}")