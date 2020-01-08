
import math

def distance(a,b):
	return round(math.sqrt(a*a+b*b),3) 

x = int(input("value of x : "))
y = int(input("value of y : "))
print (distance(x,y))