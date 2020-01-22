from Utility import utility


try:
    
    dequeue = utility.Dequeue()
    input_string = str(input("Enter the string : "))
    for character in input_string:
        dequeue.addFront(character)
    print(dequeue.removeFront())
    print(dequeue.size())
    dequeue.dispaly_dequeue_list()


except ValueError:

    print("Error")