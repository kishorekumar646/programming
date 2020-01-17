import cmath

"""      the roots of the equation a*x*x + b*x + c. Since the equation is x*x, hence there are 2 roots. 
         The 2 roots of the equation can be found using a formula (Note: Take a, b and c as input values)
         
         delta = b*b - 4*a*c
         Root 1 of x = (-b + sqrt(delta))/(2*a)
         Root 2 of x = (-b - sqrt(delta))/(2*a)
"""

def find_theQuadraticEquation(a,b,c):

     #finding the delta value
    delta = (b**2)-(4*a*c)

    #finding the root1 from Quadratic Equation
    root1 = (-b + cmath.sqrt(delta))/(2*a)

    #finding the root2 from Quadratic Equation
    root2 = (-b - cmath.sqrt(delta))/(2*a)
 
    print(delta)
    print("{0} and {1}".format(root1,root2))

try:

    input_of_a = int(input("enter a = "))
    input_of_b = int(input("enter a = "))
    input_of_c = int(input("enter c = "))
    find_theQuadraticEquation(input_of_a,input_of_b,input_of_c)

except ValueError:

    print("Enter Integers only !")