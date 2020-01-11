

def Anagrams(arr):
    anagram_list = []
    for i in arr:
        for j in arr:
            if (i != j) and (sorted(str(i)) == sorted(str(j))):
                anagram_list.append(i)
    print(anagram_list)



start = int(input("Enter range number\nstart : "))
end = int(input("end : "))
lst = []
for i in range(start,end+1):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            lst.append(i)
print(lst)
Anagrams(lst)