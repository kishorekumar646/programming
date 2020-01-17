def anagramCheck(s,s1):

    if sorted(s) == sorted(s1):
        return True
    else:
        return False

str1 = str(input("Enter the string1 : "))
str2 = str(input("Enter the string2 : "))
if anagramCheck(str1,str2):
    print("Is Anagram")
else:
    print("Is not Anagram")