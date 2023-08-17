email = input("Enter the email :")
password = input("Enter the password :")

login_email = "libin3636@gmail.com"
login_password = "12345"

if email == login_email and password == login_password :
    print ("You logged in successfully")

elif email != login_email and password == login_password:
    print ("Your email is wrong")

elif email == login_email and password != login_password :
    print ("Your password is wrong")

else :
    print ("You are not authenticated")

