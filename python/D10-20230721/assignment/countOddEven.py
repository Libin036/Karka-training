numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]

even=0
odd=0

even_list=[]
odd_list=[]

for i in numbers:
    if i%2==0:
        even +=1
        even_list.append(i)
        
    else:
        odd +=1
        odd_list.append(i)

print('Even numbers count :',even)
print('Odd numbers count :',odd)
print(even_list)
print(odd_list)