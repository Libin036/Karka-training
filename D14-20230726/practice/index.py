""" def function_name(): """
"""     print('I am called')

function_name()

def add():
    first_name = 'Libin'
    last_name = 'L'
    print(first_name +' '+ last_name)

add()

def combin_name(a,b):
    print(a+' '+b)
"""  """
combin_name('Libin','L')
"""  """
combin_name('Karka','Academy') """

""" 
first_name = input('Enter first name :')
last_name = input('Enter last name :')

def combine_name(a,b):
    print(a+' '+b)

combine_name(first_name,last_name) """

""" gender = input('Enter your gender :')

def gen(a):
    if a == 'male':
        print('Your color is blue')
    
    elif a == 'female':
        print('Your color is pink')

    else:
        print('invalid gender')

gen(gender) """

f_num = int(input('Enter first number :'))
s_num = int(input('Enter second number :'))

def odd_even(num):
        if num%2==0:
            print(num,'is even')

        else:
            print(num,'is odd')


def find_max(f,s):

    
    if f > s:
        print(f,'is maximum')
        odd_even(f)
        
    elif f == s:
        print("Both numbers are equal")
        odd_even(f)
        
    else:
        print(s,'is maximum')
        odd_even(s)

find_max(f_num,s_num)



