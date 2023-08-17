mixedList = [1, 2.0, "hai", "@", 5, 6, "&", 8, 9 ]

count=0

for i in mixedList:
    if type(i)==int:
        count += 1
    

print(count)