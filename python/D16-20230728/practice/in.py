List = [1,2,1,3,3,5,10,10,10,7,1]

dup_list = []

for i in range(len(List)-1):

    if List[i]==List[i+1]:
        if List[i] not in dup_list:
            dup_list.append(List[i])

print(dup_list)




