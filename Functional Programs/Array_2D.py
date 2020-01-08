rows = int(input("Enter the rows size : "))
col  = int(input("Enter the col size : "))
lst = [[int(input()) for i in range(rows)] for j in range(col)]
for i in range(rows):
	for j in range(col):
		print(lst[i][j],end=" ")
	print()
print()