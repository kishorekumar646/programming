import cmath

def find_theQuadraticEquation(a,b,c):
    delta = (b**2)-(4*a*c)    #finding the delta value
    root1 = (-b + cmath.sqrt(delta))/(2*a)  #finding the root1 from Quadratic Equation
    root2 = (-b - cmath.sqrt(delta))/(2*a)  #finding the root2 from Quadratic Equation
    print(delta)
    print("{0} and {1}".format(root1,root2))

try:
    input_of_a = int(input("enter a = "))
    input_of_b = int(input("enter a = "))
    input_of_c = int(input("enter c = "))
    find_theQuadraticEquation(input_of_a,input_of_b,input_of_c)
except ValueError:
    print("Enter Integers only !")