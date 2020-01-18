lower = int(input("enter lower range value:"))
upper = int(input("enter lower range value:"))
my_list=[]
for val in range(lower,upper+1):
    if val>1:
        for n in range(2,val):
            if (val%n) == 0:
                break
        else:
            my_list.append(val)
#print(my_list)
def anagramnumbers(my_list):
    anagram_list=[]
    for i in my_list:
        for j in my_list:
            if (i != j) and  (sorted(str(i))==sorted(str(j))):
                anagram_list.append(i) 
    return anagram_list 
print(anagramnumbers(my_list))
def palindromenumbers(my_list):
    palindrome_list=[]
    for i in my_list:
            if(str(i)==str(i)[::-1]):
                palindrome_list.append(i) 
    return palindrome_list 
print(palindromenumbers(my_list))