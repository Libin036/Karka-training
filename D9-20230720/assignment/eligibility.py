maths=int(input("Enter the maths mark :"))
physics=int(input("Enter the physics mark :"))
chemistry=int(input("Enter the chemistry mark :"))

mat_phy_chem=maths+physics+chemistry
print("Maths+Physics+Chemistry=",mat_phy_chem)
mat_phy=maths+physics
print("Maths+physics=",mat_phy)

if maths>=65 and physics>=55 and chemistry>=50:
    if mat_phy_chem>=190 or mat_phy>=140:
        print("You are eligible")
    else:
        print("You are not eligible")
else:
    print("You are not eligible")