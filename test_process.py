import unittest
from process import*

class TestProcess (unittest.TestCase):

    def test_init_name (self):
        '''
        Creating a process with just a name (check the attributes pid, cycles, link, and prev)
        '''
        process1 = Process ('A')
        self.assertEqual(process1.pid,'A',f'The pid should be A')
        self.assertEqual(process1.cycles,100,f'Default cycles should be 100')
        self.assertEqual(process1.prev,None,f'The process shouldn\'t be linked to any other process in the front.')
        self.assertEqual(process1.link,None,f'The process shouldn\'t be linked to any other process in the front.')
    
    def test_init_name_and_cycles (self):
        '''
        Creating a process with a name and cycles. Check the attributes pid, cycles, link, and prev
        '''
        process1 = Process ('A',20)
        self.assertEqual(process1.pid,'A',f'The pid should be A')
        self.assertEqual(process1.cycles,20,f'The cycle should be 20')
        self.assertEqual(process1.prev,None,f'The process shouldn\'t be linked to any other process in the front.')
        self.assertEqual(process1.link,None,f'The process shouldn\'t be linked to any other process in the front.')

    def test_eq (self):
        '''
        eq() - two different process objects with the same pid compare as equal (use self.assertEqual());
        two process objects with different pids compare as not equal (use self.assertNotEqual())
        '''
        process1 = Process ('A',20)
        process2 = Process ('A',30)
        self.assertEqual(process1,process2,f'The two processes are equal')

        process3 = Process ('B',40)
        self.assertNotEqual(process1,process3,f'The two processes are not equal')
    
    def test_repr (self):
        '''
        Check the match of string representationrepresentation
        '''
        process1 = Process ('A',20)
        process2 = Process ('B',30)

        self.assertEqual(repr(process1),f'Process(A, 20)')
        self.assertEqual(repr(process2),f'Process(B, 30)')

if __name__ == '__main__':
    unittest.main()