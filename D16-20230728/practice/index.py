user_details = [
                {
                    'name':'Libin',
                    'email':'libin@gmail.com',
                    'password':'libin@12',
                    'hobbies':['cricket','football','volleyball'],
                    'friendsList':['anish','hameed','kewin']
                },
                {
                    'name':'Anish',
                    'email':'anish@gmail.com',
                    'password':'anish@12',
                    'hobbies':['football','volleyball','kabadi'],
                    'friendsList':['gokul','subash','kewin']
                },
                {
                    'name':'Kewin',
                    'email':'kewin@gmail.com',
                    'password':'kewin@12',
                    'hobbies':['cricket','football','volleyball'],
                    'friendsList':['adlin','hameed','reegan']
                },
                {
                    'name':'Hameed',
                    'email':'hameed@gmail.com',
                    'password':'hameed@12',
                    'hobbies':['chess','football','kabadi'],
                    'friendsList':['saju','meshak','jewa']
                }
            ]

user_email = input('Enter the email :')
user_password = input('Enter the password :')


for detail in user_details:
    def checkUser():
        if user_email==detail['email'] and user_password==detail['password']:
            return True
        
        else:
            return False
        
    if checkUser()==True:
        detail.update({'loggedIn':True})
        print(detail['name'],'/',detail['email'])
        print('Your hobbies are :',detail['hobbies'])
        print('Your friends list are :',detail['friendsList'])

    elif checkUser()==False:
        detail.update({'loggedIn':False})


print(user_details)
