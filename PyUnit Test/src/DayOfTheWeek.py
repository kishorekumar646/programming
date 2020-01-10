
def dayOfTheWeek(arr):
	t = [0,3,2,5,0,3,5,1,4,6,2,4]
	day,month,year = int(arr[0]),int(arr[1]),int(arr[2])
	return (year + year//4 - year//100 + year//400 + t[month-1] + day) % 7

def func():
	return True

# 	def week(self,target):
# 		switcher = {
# 			0 : "SUNDAY",
# 			1 : "MONDAY",
# 			2 : "TUESDAY",
# 			3 : "WEDNESDAY",
# 			4 : "THURSDAY",
# 			5 : "FRIDAY",
# 			6 : "SATURDAY"
# 		}
# 		return switcher.get(target,"nothing")

# if __name__ == "__main__":
# 	try:
# 		date = str(input("Enter the date DD-MM-YYYY : ")).split("-")
# 		if len(date) <= 1:
# 			raise ValueError
# 		d = Day()
# 		f=d.dayOfTheWeek(date)
# 		print("\nThe day is : ",d.week(f),"\n")
# 	except ValueError:
# 		print("\nThe date format should be like this DD-MM-YYYY\n")