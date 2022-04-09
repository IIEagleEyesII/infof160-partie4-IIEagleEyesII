import time
class Minuterie :
    def __init__(self,time=2):
        self.time= time

    def run(self):
        time.sleep(self.time)
        return ""