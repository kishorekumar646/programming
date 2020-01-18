import re 
from datetime import date
Str = "hello <<name>>,"
Str1 = "We have your full name as <<Fullname>> in our system. "
Str2 ="your contact number is 91-xxxxxxxxxx. "
Str3 ="Please,let us know in case of any clarification Thank you BridgeLabz xx/xx/xxxx. "
name = input("enter name:")
surname = input("enter surname:")
contact = input("enter contact number:")
today = date.today()
d = today.strftime("%d/%m/%y")
x = re.sub("<<name>>",name,Str)
y = re.sub("<<Fullname>>",name+" "+surname,Str1)
z = re.sub("xxxxxxxxxx",contact,Str2)
w = re.sub("xx/xx/xxxx",d,Str3)
print(x+y+z+w)