from itertools import permutations

def permutationofstring(string):
    
    permlist = permutations(string)
    for perm in list(permlist):
        print("".join(perm))

string = "kai"
permutationofstring(string)