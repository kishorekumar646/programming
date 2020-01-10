def showing_windChill(temperature,speed):
    if(temperature<=50 and (speed>=3 and speed<=120)):
        windChill = (35.74+(0.6215*temperature)+((0.4275*temperature) - 35.75)*(speed**0.16))
        print("WindChill = {}".format(windChill))
    else:
        print("please enter valid input")

try:
    input_temperature = int(input("Enter the temperature : "))
    input_speed = int(input("Enter the speed : "))
    showing_windChill(input_temperature,input_speed)
except ValueError:
    print("Enter Integers only ! ")