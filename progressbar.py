import time
import sys

class ProgressBar:
    def __init__(self, max,  iterator = "#", message = "Progress"):
        self.message = message
        self.iterator = iterator
        self.init_time = time.time()
        self.end_time = None
        self.iterations = int(max/30)
        self.k = 0
        
    def start(self):
        sys.stdout.write("| {} |".format(self.message))
        
    def step(self):
        self.k = self.k+1
        if(self.k == self.iterations):
            sys.stdout.write("{}".format(self.iterator))
        if(self.k > self.iterations):
            self.k = 0

    def end(self):
        self.end_time = time.time()
        total_elapsed_time = self.end_time-self.init_time
        sys.stdout.write("| ended in {:.2f} seconds.".format(total_elapsed_time))
        
