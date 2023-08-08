amount = int(input("Enter your amount of the item : "))

if amount > 500 and amount <= 1000 :
    print ("You have owned a silver token")

elif amount > 1000 and amount < 5000 :
    print ("You have owned a golden token")

elif amount >= 5000 :
    print ("You have owned a platinum token")

else :
    print ("No token available")
