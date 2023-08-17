salary=int(input("Enter you salary :"))

if salary<10000:
    hra=salary*.20
    da=salary*.05
    gross_salary=salary+hra+da
    print("Your gross salary is",gross_salary)

elif salary>=10000 and salary<=20000:
    hra=salary*.25
    da=salary*.07
    gross_salary=salary+hra+da
    print("Your gross salary is",gross_salary)

elif salary>20000:
    hra=salary*.30
    da=salary*.08
    gross_salary=salary+hra+da
    print("Your gross salary is",gross_salary)