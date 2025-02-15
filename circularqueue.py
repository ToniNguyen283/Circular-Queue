from process import Process

class CircularQueue:
    """A circular queue to allow us to run processes turn-by-turn"""

    def __init__ (self,process:list[Process] | None =None ) -> None:
        '''
        Create attributes for the Circular Queue
        _head - first process in queue, None in an empty queue.
        _len is empty
        dictionary to control all the elements for later use
        '''
        self._head = None
        self._len = 0
        self._d_processes = dict()

        if process is not None:
            for i in process:
                self.add_process(i)
    
    def __len__ (self):
        '''
        Return the length of the Circular queuequeue
        '''
        return self._len
    
    def __repr__ (self):
        '''
        Return string representationrepresentation
        '''
        if self._len==0:
            return f'CircularQueue()'
        process_list = []
        current=self._head
        for i in range (self._len):
            process_list.append(repr(current))
            current=current.link
        return f'CircularQueue({", ".join(process_list)})'
    
    def add_process (self,process):
        '''
        adds process to end of queue (just before self._head). If a process is the only process
        in a circular queue (i.e. len(self) == 1), it’s link and prev attributes should point to itself (see
        diagram below)
        '''
        if self._head is None:
            self._head=process
            process.link=self._head
            process.prev=self._head
        else:
            last = self._head.prev
            last.link = process
            process.prev=last
            self._head.prev=process
            process.link=self._head    
        self._len+=1
        self._d_processes[process.pid]=process
    
    def remove_process (self,process):
        '''
        removes and returns a specified Process from the queue. Note that the input
        here is the actual Process object which should be removed, not its pid. See kill() for removing based
        on pid.
        '''
        if self._head is None:
            raise RuntimeError(f'Cannot remove an empty Circular Queue')
        else:
            current = self._head
            for i in range (self._len):
                if current is process:
                    if self._len ==1:
                        self._head=None
                    else:
                        current.prev.link = current.link
                        current.link.prev = current.prev
                        if current == self._head:
                            self._head=current.link
                    self._len-=1
                    self._d_processes.pop(current.pid,None)
                    return current
                current=current.link
             
    def kill_process (self,pid):
        '''
        removes and returns a process with the given pid.
        '''
        if self._len==0:
            raise RuntimeError(f'Cannot kill an empty CircularQueue')
        process = self._d_processes.get(pid,None)
        return self.remove_process(process)

    def run(self, n_cycles):
        """Runs circular queue for n_cycles, giving each process 1 cycle at a time"""
        n_remaining = n_cycles
        return_strings = []   # Using an intermediate list since appending to a string is O(n)

        while n_remaining:
            self._head.cycles -= 1

            if self._head.cycles == 0:
                return_strings.append(f"{self._head.pid} finished after {n_cycles-n_remaining+1} computational cycles.")
                self.remove_process(self._head)

            else:
                self._head = self._head.link
            
            n_remaining -= 1

        return '\n'.join(return_strings)
