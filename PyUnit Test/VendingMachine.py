def vendingMachine(value):
	notes = [1000,500,100,50,10,5,2,1]
	noteCounter = [0,0,0,0,0,0,0,0]
	print("Currency count --> ")

	for i,j in zip(notes,noteCounter):
		if value >= 1:
			print(i)
			j = value // i
			value = value - j * i
			if j != 0:
				print(i," : ",j)

amount = int(input("Enter the amount : "))
vendingMachine(amount)