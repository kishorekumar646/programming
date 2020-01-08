
import math

def distance(a,b):
	return round(math.sqrt(a**2 + b**2),3) 

x = int(input("value of x : "))
y = int(input("value of y : "))
print (distance(x,y))