import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

# QUEUE - EVERYTHING HAPPENS IN THE FRONT 
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # enqueue = add something to the back
        self.size += 1
        return self.storage.add_to_tail(ListNode(value))


    def dequeue(self):
        # dequeue = delete something in the front 
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
        # temp = self
        # count = 0 
        # while temp is not None:
        #     count += 1 
        #     temp = temp.next 
        # return count
