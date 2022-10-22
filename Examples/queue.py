class QueueError(IndexError):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.__q = []

    def put(self, elem):
        self.__q.insert(0, elem)

    def get(self):
        val = self.__q[-1]
        del self.__q[-1]
        return val


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")
