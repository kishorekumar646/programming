from itertools import permutations

def permutation_of_string(string):
    
    permlist = permutations(string)
    
    for perm in list(permlist):
        print("".join(perm))


try:
    string_input = str(input("Enter the string : "))
    permutation_of_string(string_input)

except ValueError:
    print("Error")