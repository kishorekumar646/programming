from itertools import permutations

def permutationofstring(string):
    
    permlist = permutations(string)
    
    for perm in list(permlist):
        print("".join(perm))


try:
    string_input = str(input("Enter the string : "))
    permutationofstring(string_input)

except ValueError:
    print("Error")