"""   I/P   -> Take User Name as Input. Ensure UserName has min 3 char
      Logic -> Replace UserName with the proper name
      O/P   -> Print the String with User Name      """

name = str(input("Enter your name : "))
string = "Hello username, How are you?"
print(string.replace("username",name,1))