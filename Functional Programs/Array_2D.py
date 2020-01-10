def displaying_2D_Array(array,rows,col):
	for i in range(rows):
		for j in range(col):
			print(array[i][j],end=" ")
		print()
	print()

try:
	rows_size = int(input("Enter the rows size : "))
	col_size  = int(input("Enter the col size : "))
	lst = [[int(input()) for i in range(rows_size)] for j in range(col_size)]  #here taking the 2D array elements
	displaying_2D_Array(lst,rows_size,col_size)
except ValueError:
	print("Enter only Integers")