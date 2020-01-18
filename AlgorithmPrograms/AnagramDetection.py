"""
    One string is an anagram of another if the second is simply a rearrangement of the first. 
    For example, 'heart' and 'earth' are anagrams...

"""

def anagramCheck(s,s1):

    if sorted(s) == sorted(s1):
        return True
    
    else:
        return False


try:

    first_input_string = str(input("Enter the string1 : "))
    second_input_string = str(input("Enter the string2 : "))

    if anagramCheck(first_input_string,second_input_string):
        print("Is Anagram")

    else:
        print("Is not Anagram")

except ValueError:
    
    print("Error")