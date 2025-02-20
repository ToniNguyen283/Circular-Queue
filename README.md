# Circular-Queue

Overview: 
This project implements a Circular Queue ADT to simulate an operating system managing multiple processes on a single CPU. The queue is structured as a doubly linked list with a circular connection, allowing for efficient process scheduling and management. The implementation ensures O(1) process removal using a dictionary-based lookup system.

Language: Python
Data Structures: Doubly LinkedList

Special key features:
+ Circular doubly linked list with a single head, no tail
+ The last node links back to the head, maintaining a continuous cycle
+ O(1) process removal using a dictionary (pid: process mapping)
