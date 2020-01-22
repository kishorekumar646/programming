from Utility import utility

class Banking_cash_counter:

    def __init__(self):
        
        self.bank_balance = 5000

    def deposite_amount(self,money):
        
        self.bank_balance += money
        print("\n\t--------  Succussfully deposite in your account  --------\n")

    def withdraw_amount(self,money):
        if self.bank_balance >= money:
            self.bank_balance -= money
            print("\n\t--------  Succussfully draw your money  --------\n")
        
        else:
            print("\n\t -------  You can't withdraw  ---------\n")
            print("\tBank balance is : ",self.bank_balance)
            print()

    def bank_balance_amount(self):
        
        return self.bank_balance

try:

    queue = utility.Queue()

    bank = Banking_cash_counter()
    panel_size = int(input("Enter the panel size : "))
    for person in range(panel_size):
        queue.enqueue(person)
    queue.dispaly_queue_list()
    
    print("1.Deposit\t2.Withdraw\t3.Bank Balance\t4.terminate")
    
    b = True
    
    while b:
        print("{} person ".format)
        choice = int(input("Enter your choice : "))

        if choice == 1:
            amount = int(input("Enter amount to deposite : "))
            bank.deposite_amount(amount)

        elif choice == 2:
            if bank.bank_balance > 0:
                amount = int(input("Enter amount to withdraw : "))
                bank.withdraw_amount(amount)

            else:
                print("Bank balance not available")
                bank.bank_balance = 0

        elif choice == 3:
            print("Bank balance : ",bank.bank_balance_amount())

        elif choice == 4:
            b = False
            print("\n\t--------  Succussfully stored data  --------\n")

        else:
            print("Wrong input please try again")

except ValueError:

    print("Error")