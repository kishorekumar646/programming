from Utility import utility

try:

    # input_parenthesis = str(input("Enter parenthesis expression : "))

    stack = utility.Stack()

    print("1.Insert\t2.Display List\t3.Top Element\t4.Delete\t5.Terminate")
    b = True
    while b:
        choice = int(input("Enter your choice : "))
        if choice == 1:
            item = int(input("Enter the number : "))
            stack.push(item)
        
        elif choice == 2:
            stack.dispaly_stack_list()
        
        elif choice == 3:
            print("Top element is : ",stack.peek())

        elif choice == 4:
            print("Delete element is : ",stack.pop())

        elif choice == 5:
            b = False
            print("  --------  Close Stack  -------")
        else:
            print("Wrong input")
except ValueError:

    print("Error")