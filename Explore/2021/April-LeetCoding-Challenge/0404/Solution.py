class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [-1 for _ in range(k)]
        self.length = 0
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.queue[self.rear] = value
        self.length += 1
        self.rear = (self.rear+1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.queue[self.front] = -1
        self.length -= 1
        self.front = (self.front+1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.rear-1]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.size == self.length


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
