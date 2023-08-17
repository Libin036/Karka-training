# Finding the largest number
"""
num1=int(input("Enter a first number :"))
num2=int(input("Enter a second number :"))
num3=int(input("Enter a third number :"))

if num1>num2 and num1>num3:
    print(num1,"is greater")
     
elif num2>num1 and num2>num3:
    print(num2,"is greater")

else:
    print(num3,"is greater")
"""
# without using and or not ,finding largest number

num1=int(input("Enter a first number :"))
num2=int(input("Enter a second number :"))
num3=int(input("Enter a third number :"))

if num1>num2:
    if num1>num3:
        print(num1)

elif num2>num3:
    if num2>num1:
        print(num2)

else:
    print(num3)
