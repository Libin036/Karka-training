#condition Statement
"""
gender = input("Enter your gender :")

if gender == "male":
    print ("Blue")

elif gender == "female":
    print ("Pink")

elif gender =="transgender":
    print ("Lavender")

else:
    print ("Invalid")



login = "True"

if login == "True":
    print ("Go to Home page")

else: 
    print ("invalid")
"""

# Adding multiple Statements  in a condition

total_mark = int(input("Enter your mark : "))

if total_mark > 92 :
    print ("You are eligible for MBBS")

elif total_mark > 85 and total_mark <= 92 :
    print ("You are eligible for BDS")

elif total_mark > 75 and total_mark <= 85 :
    print ("You are eligible for Agri")

else :
    print ("You are eligible for Engenering")

