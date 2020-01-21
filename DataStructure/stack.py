from Utility import utility

def check_balanced_parenthesis(parenthesis_string):

    stack = utility.Stack()

    for token in parenthesis_string:

        if (token == '(') or (token == '{') or (token == '['):
            stack.push(token)
        
        else:
            top_list = stack.pop()

            if top_list == '(':
                if (token == '}') or (token ==']'):
                    return False
            
            if top_list == '[':
                if (token == '}') or (token ==')'):
                    return False
            
            if top_list == '{':
                if (token == ')') or (token ==']'):
                    return False

    if stack.isEmpty:
        return True
    else:
        return False

try:

    input_parenthesis = str(input("Enter parenthesis expression : "))
    if check_balanced_parenthesis(input_parenthesis):
        print(input_parenthesis," is Balanced")
    
    else:
        print(input_parenthesis," is Not Balanced")

    
except ValueError:

    print("Wrong input")