friend_details = [ {"name":"Libin",
                    "place":"Ammandivilai",
                    "hobbies":["Bike Riding","volley ball","Running"]
                    },
                   {"name":"Delma",
                    "place":"Midalam",
                    "hobbies":["Drawing","Gardening","Chess"]
                    },
                   {"name":"Vikash",
                    "place":"Peruvilai",
                    "hobbies":["cricket","Kabadi","gym"]
                    },
                   {"name":"Renitha",
                    "place":"Toophur",
                    "hobbies":["Playing Games","Watching TV","Gardening"]
                    },
                   {"name":"Ratheesh"
                    ,"place":"Perunthurai",
                    "hobbies":["cricket","volley ball","gym"]
                    },
                   {"name":"Vinish"
                    ,"place":"Poothapandi",
                    "hobbies":["foot ball","handball","pubg"]
                    },
                   {"name":"Hari",
                    "place":"Monday Market",
                    "hobbies":["kabadi","cricket","Volley ball"]
                    },
                   {"name":"Mohmed Azim"
                    ,"place":"Tittuvilai",
                    "hobbies":["kabadi","cricket","Volley ball"]
                    } 
                ]

friend_details.append({"name":"Anish",
                        "place":"Ammandivilai",
                        "hobbies":["kabadi","cricket","Volley ball"]
                      })
""" hobby = input("enter a hobby :")

for i in friend_details:
    i['hobbies'].append('coding')
    for a in i["hobbies"]:
        if a == hobby:
            print(i['name']) """

hobbies_list = []

for i in friend_details:
    for a in i["hobbies"]:
        hobbies_list.append(a)

print(hobbies_list)




    