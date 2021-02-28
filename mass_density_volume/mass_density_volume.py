to_find=input("Which one to claculate (mass(m) / volume(v) / density(d))? ")
if to_find=='m':
    den=float(input("Enter the Density: "))
    vol=float(input("Enter the Volume: "))
    print("Mass=",den*vol)
elif to_find=='v':
    den=float(input("Enter the Density: "))
    mass=float(input("Enter the Mass: "))
    print("Volume=",mass/den)
elif to_find=='d':
    mass=float(input("Enter the Mass: "))
    vol=float(input("Enter the Volume: "))
    print("Density=",mass/vol)
else:
    print("Enter either 'm' or 'v' or 'd'")