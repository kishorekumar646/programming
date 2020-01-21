from Utility import utility

try:

    queue = utility.Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    queue.dispaly_queue_list()

    queue.dequeue()
    queue.dispaly_queue_list()
    queue.dequeue()
    queue.dispaly_queue_list()
    queue.dequeue()
    queue.dispaly_queue_list()
    queue.dequeue()
    queue.enqueue(10)
    queue.dispaly_queue_list()

except ValueError:
    print("Error")