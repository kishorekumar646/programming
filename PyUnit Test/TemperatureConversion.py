try:
	b = True
	print("1.Celsius to Fahrenheit\t2.Fahrenheit to Celsius\t3.terminate\n")
	while b:
		n = int(input("Enter your choice : "))
		if n == 1:
			celsius = float(input("Enter temperature in celsius: "))
			fahrenheit = (celsius * 9/5) + 32
			print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
		elif n == 2:
			fahrenheit = float(input("Enter temperature in fahrenheit: "))
			celsius = (fahrenheit - 32) * 5/9
			print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))
		elif n == 3:
			b = False
		else:
			raise ValueError
except ValueError:
	print("Wrong Input!")