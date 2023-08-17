unit = int(input("Enter the electricity units :"))
cost = int(input("Enter the cost per unit :"))

if unit<=100:
    units_charge=unit*cost
    gst_charge=units_charge*.18
    total_charge=units_charge+gst_charge
    print("Your total electricity cost is",total_charge)

elif unit>100 and unit<=500:
    units_charge=unit*cost
    extra_charge=units_charge+50
    gst_charge=extra_charge*.18
    total_charge=extra_charge+gst_charge
    print("Your total electricity cost is",total_charge)

elif unit>500 and unit<=1000:
    units_charge=unit*cost
    extra=units_charge*.05
    extra_charge=units_charge+extra
    gst_charge=extra_charge*.18
    total_charge=extra_charge+gst_charge
    print("Your total electricity cost is",total_charge)