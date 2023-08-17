user_foods = {"milk":1.02,"popcorn":2.5,"bread":2.5}
foods = list(user_foods)

food1 =input("Order your first food :")
food2 =input("Order your second food :")

if food1==foods[0] or food1==foods[1] or food1==foods[2]:
    if food2==foods[0] or food2==foods[1] or food2==foods[2]:
        if food1=="milk":
            print("Cost of the milf =",user_foods["milk"])
        elif food1=="popcorn":
            print("Cost of thre popcorn =",user_foods["popcorn"])
        elif food1=="bread":
            print("Cost of thre bread =",user_foods["bread"])
        
        if food2=="milk":
            print("Cost of the milf =",user_foods["milk"])
        elif food2=="popcorn":
            print("Cost of thre popcorn =",user_foods["popcorn"])
        elif food2=="bread":
            print("Cost of thre bread =",user_foods["bread"]) 

if  food1==foods[0] and food2==foods[0]:
    total=user_foods["milk"]+user_foods["milk"]
    print("Total cost=",total)
elif food1==foods[1] and food2==foods[1]:
    total=user_foods["popcorn"]+user_foods["popcorn"]
    print("Total cost=",total)
elif food1==foods[2] and food2==foods[2]:
    total=user_foods["bread"]+user_foods["bread"]
    print("Total cost=",total)
elif food1==foods[0] and food2==foods[1]:
    total=user_foods["milk"]+user_foods["popcorn"]
    print("Total cost=",total)
elif food1==foods[0] and food2==foods[2]:
    total=user_foods["milk"]+user_foods["bread"]
    print("Total cost=",total)
elif food1==foods[1] and food2==foods[0]:
    total=user_foods["popcorn"]+user_foods["milk"]
    print("Total cost=",total)
elif food1==foods[1] and food2==foods[2]:
    total=user_foods["popcorn"]+user_foods["bread"]
    print("Total cost=",total)
elif food1==foods[2] and food2==foods[0]:
    total=user_foods["bread"]+user_foods["milk"]
    print("Total cost=",total)
elif food1==foods[2] and food2==foods[1]:
    total=user_foods["bread"]+user_foods["popcorn"]
    print("Total cost=",total)


else:
    print("Item is not available") 

