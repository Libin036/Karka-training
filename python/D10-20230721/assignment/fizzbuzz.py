num = int(input("Enter a number :"))

if num%5==0 and num%3==0:
    print("Fizz buzz")

elif num%5==0:
    print("Buzz")

elif num%3==0:
    print("Fizz")

else:
    print(num)
    