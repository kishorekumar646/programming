"""
	A library for reading in 2D arrays of integers input and printing them out to standard output.

"""

def displaying_2D_Array(array,rows_size,column_size):
	
	for row in range(rows_size):
		for column in range(column_size):
			print(array[row][column],end=" ")
		print()
	print()

try:

	input_rows_size = int(input("Enter the rows size : "))
	input_column_size  = int(input("Enter the col size : "))

	#here taking input the 2D array elements
	array_list = [[int(input()) for row_number in range(input_rows_size)] for column_number in range(input_column_size)]
	displaying_2D_Array(array_list,input_rows_size,input_column_size)

except ValueError:

	print("Enter only Integers")