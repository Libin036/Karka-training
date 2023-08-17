items_list = [
    {'name': 'Apple', 'category': 'Fruits'},
    {'name': 'Carrot', 'category': 'Vegetables'},
    {'name': 'Banana', 'category': 'Fruits'},
    {'name': 'Broccoli', 'category': 'Vegetables'},
    {'name': 'Mango', 'category': 'Fruits'},
    {'name': 'Tomato', 'category': 'Vegetables'},
    {'name': 'Orange', 'category': 'Fruits'}
]

""" def fruits(items):

    fruits_list = []

    for i in items:
        if i['category']=='Fruits':
            fruits_list.append(i['name'])
    return fruits_list
        
def vegetables(items):

    vegetables_list = []

    for i in items:
        if i['category']=='Vegetables':
            vegetables_list.append(i['name'])
    return vegetables_list
        

print({'Fruits':fruits(items_list),'Vegetables':vegetables(items_list)}) """


""" def grouping_by_categ(List):

    fruits_list = []
    vegetables_list = []
    result={'Fruits':fruits_list,'Vegetables':vegetables_list}

    for i in List:
        if i['category']=='Fruits':
            fruits_list.append(i['name'])
        
        elif i['category']=='Vegetables':
            vegetables_list.append(i['name'])

    return result

print(grouping_by_categ(items_list)) """

def groupitems(List):

    temp={}
    for i in List:
        if i['category'] not in temp:
            temp[i['category']]=[i['name']]

        else:
            temp[i['category']].append(i['name'])

    return temp

print(groupitems(items_list))













