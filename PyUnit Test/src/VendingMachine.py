def vendingMachine_imp(value):
	notes = [1000,500,100,50,10,5,2,1]
	noteCounter = [0,0,0,0,0,0,0,0]
	print("Currency count --> ")

	for i,j in zip(notes,noteCounter):
		flag = 0
		if value >= 1:
			print(i)
			j = value // i
			value = value - j * i
			if j != 0:
				print(i," : ",j)
				flag = 1
	if flag == 1:
		return True
	else:
		return False
