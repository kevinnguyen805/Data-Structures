Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`? O(1)

2. What is the runtime complexity of `dequeue`? O(1)

3. What is the runtime complexity of `len`? 0(n) since you can only "peak" at the first item and must take out everything to see its length

## Binary Search Tree

1. What is the runtime complexity of `insert`? O(log n) because every "step" we take eliminates a number of possibilities 

2. What is the runtime complexity of `contains`? O(log n) 

3. What is the runtime complexity of `get_max`? O(n)

## Heap

1. What is the runtime complexity of `_bubble_up`? 

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`? O(n)

2. What is the runtime complexity of `ListNode.insert_before`? O(n)

3. What is the runtime complexity of `ListNode.delete`? O(n)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`? O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`? O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`? O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`? O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`? O(n) 

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`? O(n)

10. What is the runtime complexity of `DoublyLinkedList.delete`? O(n)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    The worst-case runtime of array.slice() should be O(n+k) where n is the number of elements you are counting in the array and k is the copying part of the new array 
    DLL's delete method allows you to delete items with O(n) where you must traverse to that item you want to delete, and since you have the previous and next pointer, you can delete it in constant time.
    