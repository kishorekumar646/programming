import cmath
a = int(input("enter A = "))
b = int(input("enter B = "))
c = int(input("enter C = "))

delta = (b**2)-(4*a*c)


root1 = (-b + cmath.sqrt(delta))/(2*a)

root2 = (-b - cmath.sqrt(delta))/(2*a)

print(delta)

print("{0} and {1}".format(root1,root2))
