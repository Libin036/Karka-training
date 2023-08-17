# Ticket price finding

age = int(input("Enter your age to know the ticket price :"))

if age < 3:
    print ("You can buy a free ticket")

elif age >= 3 and age <=12:
    print ("Your ticket price is $10")

elif age >= 65:
    print ("Your ticket price is $12")

else :
    print ("Your ticket price is $15")