from Utility import utility


try:
    dequeue = utility.Dequeue()

    dequeue.addFront(10)
    dequeue.addFront(20)
    dequeue.addRear(30)
    dequeue.dispaly_dequeue_list()
    dequeue.removeRear()
    dequeue.dispaly_dequeue_list()


except ValueError:

    print("Error")