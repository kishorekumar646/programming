"""    
	Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0

"""

def findsTriplets(arr):

	found = False
	
	for i in range(len(arr)-2):
		for j in range(i+1,len(arr)-1):
			for k in range(j+1,len(arr)):
				if(arr[i] + arr[j] + arr[k] == 0):
					print(arr[i]," ",arr[j]," ",arr[k])
					found = True

	if found == False:
		print("NOT FOUND")

try:

	taking_sizeOfArray = int(input("Enter the size of array : "))
	array_list = [int(input()) for value in range(taking_sizeOfArray)]
	findsTriplets(array_list)

except ValueError:
	
	print("Take integers only")