"""
    Take a range of 0 - 1000 Numbers and find the Prime numbers in that range.

"""

def Prime_numbers(start,end):

    prime_list = []
    
    for take_number in range(start,end+1):
        if take_number > 1:
            for check in range(2,take_number):
                if (take_number % check) == 0:
                    break
            else:
                prime_list.append(take_number)
  
    print(prime_list)

try:
    Prime_numbers(0,1000)

except ValueError:
    print("Error")