

fruits = ['apple','orange','grapes']

print(fruits[0])

fruits.append('pineapple')  # add
fruits[0] = 'dragon fruit'  # update
fruits.insert(1,'banana')   # insert in specified position

print(fruits)

# add two list 

row1 = ['anishh','ajay','sam']
row2 = ['kumar','libin','siva']

two_rows = row1 + row2

print(two_rows)


# add and update in dictionery

detail = { 'name':'karka',
           'place':'putheri'
         }

detail['phone'] = '367147863'  #add
detail['place'] = 'nagercoil'  #update
detail.update({'email':'hasdhja@gmail.com','website':'www.hdhvja.com'})   # it will update many keys to the dictionery

print(detail)