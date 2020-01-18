"""   I/P   -> Year, ensure it is a 4 digit number.
      Logic -> Determine if it is a Leap Year.
      O/P   -> Print the year is a Leap Year or not.          """


#here check the leap year are not 
def ifLeapYear_thenReturnTrue_otherwiseReturnFalse(year):

    if (year%4) == 0:
        if (year%100) == 0:
            if (year%400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

try:

    leap_year_input = int(input("Enter year : "))
    if ifLeapYear_thenReturnTrue_otherwiseReturnFalse(leap_year_input):
        print(leap_year_input," is leap year")
    else:
        print(leap_year_input," is not leap year")

except ValueError:

    print ("It should be an Integer ! ")