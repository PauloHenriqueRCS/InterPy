class Node:
    def __init__(self, ele=0, prev=None):
        self.ele = ele
        self.prev = prev

class Battery:
    def __init__(self): 
        self.top = None

    def add(self, ele):
        ele = Node(ele)
        ele.prev = self.top
        self.top = ele
    
    def remove(self):
        assert self.top, "this is empty"
        self.top = self.top.prev