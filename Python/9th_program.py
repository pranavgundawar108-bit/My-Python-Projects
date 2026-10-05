#program to find angle in degrees of hour hand on the clock face:

H =int(input("Enter in Hours"))
M =int(input("Enter in Minutes"))
S =int(input("Enter in Seconds"))

angle = (H*30) + (M*0.5) +(S*(1/120))
print(angle)