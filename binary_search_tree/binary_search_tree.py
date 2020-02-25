import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # >= because you must account for a node value that is equal to the given insert value (not just smaller/bigger node values) """
    def insert(self, value):
        # checking to see if we can insert value at root (if root doesn't have a value yet)
        if value < self.value: 
            if self.left == None: 
                self.left = BinarySearchTree(value)
            else: 
                return self.left.insert(value)
        elif value >= self.value: 
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    # Mistake here was not accounting for if the left/right node does not exist - explicitly returning False if it doesn't 
        # remember to use RETURN for recursive calls 
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if self.right is None:
                return False 
            else: 
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False 
            else: 
                return self.left.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value 
        else: 
            return self.right.get_max()



    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
        # preorder - N LR
        # postorder - LR N
        # inorder - L N R
    def for_each(self, cb):
        if self.value is not None:
            cb(self.value)
            if self.left is not None:
                self.left.for_each(cb)
            if self.right is not None: 
                self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
