def check(year):                 
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
    leap = int(input("Enter year : "))
    if check(leap):
        print(leap," is leap year")
    else:
        print(leap," is not leap year")
except ValueError:
    print ("Input format wrong!")