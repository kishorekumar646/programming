import math

"""    formula to calculate distance = sqrt(x*x + y*y)     """

def calculateDistance(a,b):
	return round(math.sqrt(a**2 + b**2),3) 

try:

	x = int(input("value of x : "))
	y = int(input("value of y : "))
	print (calculateDistance(x,y))

except ValueError:
	
	print("\nEnter Integer only ! \n")