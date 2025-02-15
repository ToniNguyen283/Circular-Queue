import unittest
from circularqueue import*

class TestCircularQueue (unittest.TestCase):

    def assertNodeEqual(self, node, expected, expected_prev, expected_link):
        """
        Function for use when checking each individual nodenode
        """
        self.assertEqual(node, expected)
        self.assertEqual(node.prev, expected_prev)
        self.assertEqual(node.link, expected_link)
    
    def test_init_empty(self):
        '''
        – Test: initialize empty CQ
        '''
        cq = CircularQueue()
        self.assertIs(cq._head,None,f'The head should be empty')
        self.assertEqual(cq._len,0,f'The length should be 0')

    def test_init_with_processes(self):
        '''
        – Test: initialize a CQ with a list of Process objects
        '''
        p1=Process('A',100)
        p2=Process('B',200)
        p3=Process('C',300)
        cq_list = CircularQueue ([p1,p2,p3])
        self.assertEqual(cq_list._head,p1,f'The head should be first element in the list')
        self.assertEqual(cq_list._len,3,f'The length should match the number of items in the list')
        
    def test_add_process_one (self):
        '''
        – Test: Add one process to empty CQ
        '''
        cq = CircularQueue ()
        cq.add_process(Process('A',100))
        node = cq._head
        self.assertEqual(len(cq),1,'There is only one Process')
        self.assertNodeEqual(node,Process('A',100),Process('A',100),Process('A',100))
    
    def test_add_process_two (self):
        '''
        – Test: Add two processes to empty CQ
        '''
        cq = CircularQueue ()
        p1 = Process('A',100)
        p2 = Process('B',200)
        cq.add_process(p1)
        cq.add_process(p2)
        node = cq._head
        node1 = cq._head.link
        self.assertEqual(len(cq),2,'There are two processes')
        self.assertEqual(cq._head,p1,f'The head should be the first process added to the list')
        self.assertNodeEqual(node,p1,node1,p2)
        self.assertNodeEqual(node1,p2,cq._head,cq._head)
    
    def test_add_process_three (self):
        '''
        – Test: Add three processes to empty CQ
        '''
        cq = CircularQueue ()
        p1 = Process('A',100)
        p2 = Process('B',200)
        p3 = Process('C',300)
        cq.add_process(p1)
        cq.add_process(p2)
        cq.add_process(p3)
        node = cq._head
        node1 = node.link
        node2 = node1.link
        self.assertEqual(len(cq),3,'There are two processes')
        self.assertEqual(cq._head,p1,f'The head should be the first process added to the list')
        self.assertNodeEqual(node,p1,p3,p2)
        self.assertNodeEqual(node1,p2,p1,p3)
        self.assertNodeEqual(node2,p3,p2,p1)
    
    def test_repr (self):
        '''
        – Test that you get the correct string result from a queue of 3 processes
        '''
        p1 = Process('A',100)
        p2 = Process('B',200)
        p3 = Process('C',300)
        cq = CircularQueue ([p1,p2,p3])
        self.assertEqual(repr(cq),'CircularQueue(Process(A, 100), Process(B, 200), Process(C, 300))',f'Check the repr function again')
    
    def test_remove_process_3_middle (self):
        '''
        Test: From middle of CQ with 3 or more processes
        '''
        p1 = Process('A',100)
        p2 = Process('B',200)
        p3 = Process('C',300)
        cq = CircularQueue ([p1,p2,p3])
        removed_value = cq.remove_process(p2)
        node = cq._head
        node1 = cq._head.link
        self.assertEqual(len(cq),2,'There are two processes')
        self.assertEqual(cq._head,p1,f'The head should be the first process added to the list')
        self.assertEqual(removed_value,p2,f'The method should remove the middle')
        self.assertNodeEqual(node,p1,p3,p3)
        self.assertNodeEqual(node1,p3,p1,p1)
    
    def test_remove_process_3_head (self):
        '''
        Test: From front of CQ with 3 or more processes
        '''
        p1 = Process('A',100)
        p2 = Process('B',200)
        p3 = Process('C',300)
        cq = CircularQueue ([p1,p2,p3])
        removed_value = cq.remove_process(p1)
        node = cq._head
        node1 = cq._head.link
        self.assertEqual(len(cq),2,'There are two processes')
        self.assertEqual(cq._head,p2,f'The head should be the first process added to the list')
        self.assertEqual(removed_value,p1,f'The method should remove the head')
        self.assertNodeEqual(node,p2,p3,p3)
        self.assertNodeEqual(node1,p3,p2,p2)
    
    def test_remove_process_3_final (self):
        '''
        Test: From end of CQ (just before self._head) with 3 or more processes
        '''
        p1 = Process('A',100)
        p2 = Process('B',200)
        p3 = Process('C',300)
        cq = CircularQueue ([p1,p2,p3])
        removed_value = cq.remove_process(p3)
        node = cq._head
        node1 = cq._head.link
        self.assertEqual(len(cq),2,'There are two processes')
        self.assertEqual(cq._head,p1,f'The head should be the first process added to the list')
        self.assertEqual(removed_value,p3,f'The method should remove the tail')
        self.assertNodeEqual(node,p1,p2,p2)
        self.assertNodeEqual(node1,p2,p1,p1)
    
    def test_remove_process_1 (self):
        '''
        From CQ with exactly 1 process
        '''
        p1 = Process('A',100)
        cq = CircularQueue ([p1])
        removed_value = cq.remove_process(p1)
        node = cq._head
        self.assertEqual(len(cq),0,'There are 0 process')
        self.assertIs(cq._head,None,f'The Circular Queue should be empty')
        self.assertEqual(removed_value,p1,f'The method should remove the only process in the Circular Queue')
        self.assertIsNone (cq._head,f'There should be no process')
    
    def test_kill_3_middle (self):
        '''
        kill a process in the middle of a CQ with 3 or more processes
        '''
        p1 = Process('A',100)
        p2 = Process('B',200)
        p3 = Process('C',300)
        cq = CircularQueue ([p1,p2,p3])
        removed_value = cq.kill_process(p2.pid)
        node = cq._head
        node1 = cq._head.link
        self.assertEqual(len(cq),2,'There are two processes')
        self.assertEqual(cq._head,p1,f'The head should be the first process added to the list')
        self.assertEqual(removed_value,p2,f'The method should remove the middle')
        self.assertNodeEqual(node,p1,p3,p3)
        self.assertNodeEqual(node1,p3,p1,p1)

if __name__ =='__main__':
    unittest.main()
