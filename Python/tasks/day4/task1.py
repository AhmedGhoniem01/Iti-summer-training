class Queue:
    def __init__(self):
        self.queue=[]
    
    def insert(self,value):
        self.queue.append(value)
        print(self.queue)
    
    def pop(self,value):
        if(len(self.queue) == 0):
            print("No elements to pop")
        else:
            element = self.queue.pop(0)
        print(f"Removed element {element}")
    
    def is_empty(self):
        if(len(self.queue) == 0):
            return True
        else:
            return False

q1 = Queue()
q1.insert(5)
q1.insert(10)
q1.pop(5)
print(q1.queue)
print(q1.is_empty())