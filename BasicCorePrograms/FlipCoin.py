import random

"""  I/P   -> The number of times to Flip Coin. Ensure it is positive integer.
     Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or heads
     O/P   -> Percentage of Head vs Tails                                 """

try:
	number_of_times = int(input("Enter the number : "))
	tails_count = 0
	heads_count = 0
	for i in range(number_of_times):

			#here taking the random number in float
	        taking_random_numer = round(random.random(),1)
	        print(taking_random_numer)
	        if taking_random_numer<0.5:
	            tails_count=tails_count+1
	        else:
	            heads_count=heads_count+1
	# print (tail,"  ",head)

	#here calculating tails percentage
	tails_percentage = (tails_count*100)//number_of_times

	#here calculating heads percentage
	heads_percentage = (heads_count*100)//number_of_times
	print("tails percentage : {0}\nhead percentage : {1} ".format(tails_percentage,heads_percentage))
except ValueError:
	print("It should be an Integer ! ")