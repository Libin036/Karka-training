monthly_gold_rate=[{'month':'jan',
                    'rate':2000,
                    'jewls_list':[{'name':'chain',
                              'making_charge':12},
                             {'name':'ring',
                              'making_charge':11}]
                    },
                    {'month':'feb',
                     'rate':3500,
                     'jewls_list':[{'name':'chain',
                              'making_charge':12},
                             {'name':'ring',
                              'making_charge':11}]
                     },
                    {'month':'may',
                     'rate':1900,
                     'jewls_list':[{'name':'chain',
                              'making_charge':12},
                             {'name':'ring',
                              'making_charge':11}]
                     },
                    {'month':'jun',
                     'rate':5000,
                     'jewls_list':[{'name':'chain',
                              'making_charge':12},
                             {'name':'ring',
                              'making_charge':11}]
                     },
                    {'month':'dec',
                     'rate':1000,
                     'jewls_list':[{'name':'chain',
                              'making_charge':12},
                             {'name':'ring',
                              'making_charge':11}]
                     },
                    {'month':'sep',
                     'rate':1500,
                     'jewls_list':[{'name':'chain',
                              'making_charge':12},
                             {'name':'ring',
                              'making_charge':11}]
                     }
                    ]

#Min value
""" min_value=monthly_gold_rate[0]['gold_rate']
max_value=monthly_gold_rate[0]['gold_rate']

for i in monthly_gold_rate:
    if i['gold_rate']<= min_value:
        min_value=i['gold_rate']
        min_month=i['month']

    if i['gold_rate']>= max_value:
        max_value=i['gold_rate']
        max_month=i['month']

for i in monthly_gold_rate:
        print(i['jewls']['name'])



print(min_month,'month is cheaper price',min_value)
print(max_month,'month is more price',max_value)

"""

for item in  monthly_gold_rate:
    
    print( "Gold rate is " + str(item["rate"]))
    jewls_list = item["jewls_list"]
    
    for j in jewls_list:
                        # 2000 * 13 / 100
        cal_mak_charge = item["rate"] * j['making_charge'] / 100
        final_charge = item["rate"] + cal_mak_charge
        gst_charge = final_charge*18/100
        total_charge = gst_charge + final_charge
        print(j['name'] + " rate is "+ str(total_charge))