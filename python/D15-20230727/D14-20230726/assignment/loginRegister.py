userDtails = [{
    "name" : "saravana",
    "e_mail" : "saravana@gmail.com",
    "password" : "saravan@123",
},
{
    "name" : "benish",
    "e_mail" : "benish@gmail.com",
    "password" : "benish@123",
},
{
    "name" : "kabeesh",
    "e_mail" : "kabeesh@gmail.com",
    "password" : "kabeesh@123",
},
{
    "name" : "naathan",
    "e_mail" : "naathan@gmail.com",
    "password" : "naathan@123",
}]

user_login_register = input('Login or Register :')

def user_login():
    user_name = input('Enter your user name :')
    password = input('Enter your password :')

    for detail in userDtails:
        if detail['name']==user_name and detail['password']==password:
            return 

        elif detail['name']==user_name and detail['password']!=password:
            p='invalid password'

        else:
            p='You are not registered,please register.'
    print(p)



def user_register():
    user_name = input('Enter user name :')
    user_email = input('Enter your email :')
    password = input('Enter password :')
    conf_password = input('Enter confirm password :')

    for detail in userDtails:
        if user_name == detail['name'] or user_email == detail['e_mail']:
            print('You are already registered.')

    if password == conf_password:
        userDtails.append({'name':user_name,'e_mail':user_email,'password':password})
        print('Register successful,Now you can login.')




if user_login_register == 'login':
    user_login()
    

elif user_login_register == 'register':
    user_register()
    user_login()
    
    





