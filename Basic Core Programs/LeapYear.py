def ifLeapYear_thenReturnTrue_otherwiseReturnFalse(year):   #here check the leap year are not           
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