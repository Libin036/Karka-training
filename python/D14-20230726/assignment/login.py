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

def login_fun(details):
    user_email = input('Enter your user e-mail :')
    password = input('Enter your password :')

    for det in details:
        if det['e_mail'] == user_email and det['password'] == password:
            a= 'login successful'
            break
        
        elif det['e_mail'] == user_email and det['password'] != password:
            a= 'invalid password'
            
        
        else:
            a= 'Not registered'
            
    return a


def register_fun(details):
    user_name = input('Enter user name :')
    user_email = input('Enter your email :')
    password = input('Enter password :')
    conf_password = input('Enter confirm password :')

    for det in details:
        if det['name'] == user_name and det['e_mail'] == user_email:
            print('already registered')
    
        elif password == conf_password:
            details.append({'name':user_name,'e_mail':user_email,'password':password})
            print('Registered successful')
            return details



if user_login_register == 'login':
    # login_fun(userDtails)
    print(login_fun(userDtails))

elif user_login_register == 'register':
    userDtails=register_fun(userDtails)

    print(login_fun(userDtails))
    