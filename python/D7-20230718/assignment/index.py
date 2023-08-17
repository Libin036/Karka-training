name = input("Enter your name :")
age = int(input("Enter your age :"))
gender = input("Enter your gender :")

if age > 60:
    if gender=="male":
        print ("Hi Mr.",name,",You are a senior citizen")

    elif gender=="female":
        print ("Hi Miss.",name,", You are a senior citizen")
    
    else:
        print ("Invalid gender")

elif age > 18 and age <= 60:
    if gender=="male":
        print ("Hi Mr.",name,",You are a adult")

    elif gender=="female":
        print ("Hi Miss.",name,", You are a adult")
    
    else:
        print ("Invalid gender")
    
else:
    if gender=="male":
        print ("Hi Mr.",name,",You are a teenager")

    elif gender=="female":
        print ("Hi Miss.",name,", You are a teenager")
    
    else:
        print ("Invalid gender")