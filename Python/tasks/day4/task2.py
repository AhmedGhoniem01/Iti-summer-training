from logging import exception


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


#---------------------------------------------------------------------------------------
def extended_Queue(Queue):
    length=3
    queues_num=0
    queue_obj=[]

    def __init__(self,name=""):
        Queue.__init__(self)     #super(extended_queue, self).__init__()
        self.name =name
        queue_num += 1
        queue_obj.append(self)
    
    def insert(self,value):
        if(len(self.queue) == length):
            raise exception("QueueOutOfRangeException!")
        else:
            Queue.insert(self,value)
    
    @classmethod
    def get_queue(cls,name):
        for obj in queue_obj:
            if (obj.name == name):
                return obj
        print("object not found")

q1 = extended_Queue("queue1")
q1.insert(5)
q1.insert(10)
q1.insert(11)
q1.insert(5)

# q1 = extended_Queue("queue1")
# q1.insert(5)
# q1.insert(10)
# q1.insert(11)
# q2 = extended_Queue("queue2")
# q2.insert(20)
# q2.insert(30)
# print(extended_Queue.queues_num)
# print(extended_Queue.get_queue("queue2"))





    
     
