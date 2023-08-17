"""
# List

Friend_names = [ "Vikash","Delma","Ratheesh","Renitha","Vinish","Hari","Mohamed Azim","Libin"] 

print (Friend_names)

print (Friend_names[7])

# Dictionery

my_details = {"name":"Libin" , "place":"Ammandivilai"} 

print (my_details)
print ("Name :",my_details["name"]," Place :", my_details["place"])

print (my_details["name"])


# List inside dictionery

friend_details = [ {"name":"Libin","place":"Ammandivilai"},
                   {"name":"Delma","place":"Midalam"},
                   {"name":"Vikash","place":"Peruvilai"},
                   {"name":"Renitha","place":"Toophur"},
                   {"name":"Ratheesh","place":"Perunthurai"},
                   {"name":"Vinish","place":"Poothapandi"},
                   {"name":"Hari","place":"Monday Market"},
                   {"name":"Mohmed Azim","place":"Tittuvilai"} 
                ]

print (friend_details)

print (friend_details[0])

"""

# List inside dictionery    Dictionery inside List

friend_details = [ {"name":"Libin","place":"Ammandivilai","hobbies":["Bike Riding","volley ball","Running"]},
                   {"name":"Delma","place":"Midalam","hobbies":["Drawing","Gardening","Chess"]},
                   {"name":"Vikash","place":"Peruvilai","hobbies":["cricket","Kabadi","gym"]},
                   {"name":"Renitha","place":"Toophur","hobbies":["Playing Games","Watching TV","Gardening"]},
                   {"name":"Ratheesh","place":"Perunthurai","hobbies":["cricket","volley ball","gym"]},
                   {"name":"Vinish","place":"Poothapandi","hobbies":["foot ball","handball","pubg"]},
                   {"name":"Hari","place":"Monday Market","hobbies":["kabadi","cricket","Volley ball"]},
                   {"name":"Mohmed Azim","place":"Tittuvilai","hobbies":["kabadi","cricket","Volley ball"]} 
                ]

print (friend_details[0]["name"])

print (friend_details[0]["name"],friend_details[0]["hobbies"])

print (friend_details[0]["name"],friend_details[0]["hobbies"][0])

