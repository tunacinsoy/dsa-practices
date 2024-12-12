"""
1188. Design Bounded Blocking Queue

Description:
  Implement a thread safe bounded blocking queue that has the following methods:
  BoundedBlockingQueue(int capacity): The constructor initializes the queue with a maximum capacity.
  void enqueue(int element): Adds an element to the front of the queue. If the queue is full, the calling
  thread is blocked until the queue is no longer full.
  int dequeue(): Returns the element at the rear of the queue and removes it. If the queue is empty, the calling thread is
  blocked until the queue is no longer empty.
  int size(): Returns the number of elements currently in the queue.

  Your implementation will be tested using multiple threads at the same time. Each thread will either be a producer thread
  that only makes calls to the enqueue method; or  a consumer thread that only makes calls to the dequeue method. The size method
  will be called after every test case.


Algorithm Implementation:

   1) Initialize condition lock, capacity and deque in init method.
   2) In enqueue, acquire the lock, and check for the capacity, and if the capacity is the size of deque, then wait, if not, do append,
    and notifyall.
   3) In dequeu, acquire the lock, check for the capacity, if it is 0, wait, if it is not, popleft and return the element...
"""

from collections import deque
import threading


class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        # We need condition class implementation
        self.condition = threading.Condition()
        self.capacity = capacity
        # Deque will be used for popping from the left, i.e. rear of the queue
        self.deque = deque()
        # Initially, the list will be empty, so the consumer threads has to wait
        # until there is an item appears in the deque

    def enqueue(self, element: int):
        """
        We can acquire a Condition multiple times if its underlying lock is reentrant,
        which is the case by default since threading. Condition uses RLock internally.
        """
        # With `with` block, following statements do happen:
        # Beginning -> self.condition.acquire()
        # After     -> self.condition.release()
        with self.condition:
            # While the queue is full,
            # current thread has to wait until one of the consumers consume an element from the deque
            while self.size() == self.capacity:
                # We are waiting one of the consumers to wake us up
                print("Size is full, so this thread waits...")
                self.condition.wait()

            print(f"Appending element {element}...")
            # If we are here, then we can do append operation
            self.deque.append(element)
            self.print()
            print("Notifying all waiting threads after append operation...")

            # All waiting state threads should check their condition again
            self.condition.notify_all()
            # self.condition.notify()

    def dequeue(self) -> int:

        with self.condition:

            while self.size() == 0:
                print("Size is 0, so this thread waits...")
                self.condition.wait()

            element = self.deque.popleft()
            print(f"Popping number: {element}")
            self.print()
            # time.sleep(3)
            print("Notifying all waiting threads after popleft operation...")
            # self.condition.notify()
            self.condition.notify_all()

        return element

    def size(self) -> int:
        return len(self.deque)

    def print(self):
        return print(self.deque)


def test_bounded_blocking_queue():
    solution = BoundedBlockingQueue(5)
    consumer_threads = [threading.Thread(target=solution.dequeue) for _ in range(3)]
    producer_threads = [
        threading.Thread(target=solution.enqueue, args=(i,)) for i in range(3)
    ]

    for t in consumer_threads:
        test = t.start()
    for t in producer_threads:
        t.start()
    for t in producer_threads:
        t.join()

    for t in consumer_threads:
        t.join()
    pass


test_bounded_blocking_queue()
