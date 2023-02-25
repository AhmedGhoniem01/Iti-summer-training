num = int(input("Enter number: "))
def fizz(num):
    if (num%3 == 0):
        if (num%5 == 0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif (num%5 ==0):
        print("Buzz")
fizz(num)