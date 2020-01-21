from Utility import utility

class Banking_cash_counter:

    def __init__(self):
        
        self.bank_balance = 10000

    def deposite_amount(self,money):
        
        self.bank_balance += money

    def withdraw_amount(self,money):
        
        self.bank_balance -= money

    def bank_balance_amount(self):
        
        return self.bank_balance

try:

    bank = Banking_cash_counter()
    
    print("1.Deposit\t2.Withdraw\t3.Bank Balance\t4.terminate")
    
    b = True
    
    while b:
        
        choice = int(input("Enter your choice : "))

        if choice == 1:
            amount = int(input("Enter amount to deposite : "))
            bank.deposite_amount(amount)

        elif choice == 2:
            amount = int(input("Enter amount to withdraw : "))
            bank.withdraw_amount(amount)

        elif choice == 3:
            print("Bank balance : ",bank.bank_balance_amount())

        elif choice == 4:
            b = False

        else:
            print("Wrong input please try again")

except ValueError:

    print("Error")