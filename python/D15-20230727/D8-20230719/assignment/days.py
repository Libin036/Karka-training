
# Finding Days by entering number 

num = int(input("Enter a between 1 to 7 :"))

if num>=1 and num<=7:
    if num==1:
        print("Today is sunday")

    elif num==2:
        print("Today is monday")

    elif num==3:
        print("Today is tuesday")

    elif num==4:
        print("Today is wednesday")

    elif num==5:
        print("Today is thursday")

    elif num==6:
        print("Today is friday")

    elif num==7:
        print("Today is saterday")

else:
    print ("Enter a number between 1 to 7")

# another way

num = int(input("Enter a between 1 to 7 :"))

days =["sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

print(days[num-1])

