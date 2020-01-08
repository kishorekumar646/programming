t = int(input("Enter the temp"))
v = int(input("Enter the speed "))

if(t<=50 and (v>=3 and v<=120)):

    w = (35.74+(0.6215*t)+((0.4275*t) - 35.75)*(v**0.16))
    print("W={}".format(w))
else:
    print("please enter valid input")