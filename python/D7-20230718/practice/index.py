"""
# odd or even

num = int(input("Enter a number : "))

a = num % 2

if a == 0 :
    print ("The given number is even")

else :
    print ("The given number is odd")



# Divisible or Non divisible

num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))

if num1%num2 == 0 :
    print ("Yes")

else :
    print ("No")

"""
# Leap Year

year =int(input("Enter a year :"))

if (year%400==0 and year%100==0)or(year%4==0 and year%100!=0):
    print ("It is a Leapyear")

else :
    print ("It is not a Leapyear")


