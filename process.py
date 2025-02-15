class Process:
    def __init__ (self,pid: str,cycles=100):
        '''
        Set up the attributes:
        • pid: str - a unique process identifier.
        • cycles: int - Number of clock cycles required to complete this process. This should be an optional
        parameter in init with a default value of 100.
        • link - link to the next process in a circular queue. This should not be a parameter in init, but you
        should set it to None when a process is created (e.g. self.link = None).
        • prev - as above, but for the previous process.
        '''
        self.pid=pid
        self.cycles = cycles
        self.link: Process | None =None
        self.prev: Process | None =None

        if self.prev is not None:
            self.prev.link=self
        if self.link is not None:
            self.link.prev = self
    
    def __eq__ (self,other):
        '''
        Two processes are equal if they have the same pid.
        '''
        if self.pid==other.pid:
            return True
        return False
    
    def __repr__ (self):
        '''
        Return the string representation of Process
        '''
        return f'Process({self.pid}, {self.cycles})'

