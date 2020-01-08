import random

try:
	n = int(input("Enter the number : "))
	tail = 0
	head = 0
	for i in range(n):
	        r1 = round(random.random(),1)
	        print(r1)
	        if r1<0.5:
	            tail=tail+1
	        else:
	            head=head+1
	# print (tail,"  ",head)
	tail = (tail*100)//n
	head = (head*100)//n
	print("tails percentage : {0}\nhead percentage : {1} ".format(tail,head))
except ValueError:
	print("Wrong input!")