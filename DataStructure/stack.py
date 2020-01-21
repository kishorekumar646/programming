from Utility import utility

try:

    stack = utility.Stack()
    input_parenthesis = str(input("Enter parenthesis expression : "))
    flag = 0
    for token in input_parenthesis:
        print("Token : ",token)
        if (token == '{') or (token == '(') or (token == '['):
            stack.push(token)
            stack.dispaly_stack_list()
        
        else:
            top_list = stack.pop()
            stack.dispaly_stack_list()
            print("Top : ",top_list)
            if top_list == '(':
                if (token == '}') or (token ==']'):
                    flag = 1
            if top_list == '[':
                if (token == '}') or (token ==')'):
                    flag = 1
            if top_list == '{':
                if (token == ')') or (token ==']'):
                    flag = 1
        # stack.dispaly_stack_list()
        
    if flag == 0:
        print("Balanced")
    else:
        print("Not Balanced")
    

except ValueError:

    print("Error")