a = int(input("Enter coefficient of x^2="))
b = int(input("Enter coefficient of x="))
c = int(input("Enter the constant="))

disciminant1 = ((-b+(b*b - 4 *a *c)**1/2)/2*a)
disciminant2 = ((-b-(b*b - 4 *a *c)**1/2)/2*a)

print("(discriminant1,discriminant2)",(disciminant1,disciminant2))