num1=int(input("Number 1 :"))
num2=int(input("Number 2 :"))
num3=int(input("Number 3 :"))
num4=int(input("Number 4 :"))
num5=int(input("Number 5 :"))

add_first3=num1+num2+num3
print("Added number is :",add_first3)

multiplay=add_first3*num4*num5
print("Multipliyed value is :",multiplay)

if multiplay%2==0:
    print("This number",multiplay,"is even")

else:
    print("This number",multiplay,"is odd")