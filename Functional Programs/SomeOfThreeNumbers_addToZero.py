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

n = int(input("Enter the size of array : "))
lst = [int(input()) for i in range(n)]
findsTriplets(lst)