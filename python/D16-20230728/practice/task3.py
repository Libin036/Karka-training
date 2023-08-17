userInput = input('INPUT :')

string = ''

for i in userInput:
    string = i + string

if userInput == string:
    print('It is palindrom')

else:
    print('Not a palindrom')

