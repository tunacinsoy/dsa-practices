"""
Description:

    Implement a rate limiter using leaky bucket algorithm. First, design with single-thread, and then convert the code into multithreaded.


Algorithm Implementation:
    Leaky Bucket has constant capacity, and constant drop rate.


"""

import time
import math
import threading


class LeakyBucket:
    def __init__(self, max_capacity: int, drop_rate: float):
        self.max_capacity = max_capacity
        # In terms of second -> 5 requests per second, 2 requests per second etc.
        self.drop_rate = drop_rate
        self.last_drop_check_time = time.time()
        self.current_load = 0
        self.lock = threading.Lock()

    def is_allowed(self, request_id: int) -> bool:
        with self.lock:
            print(f"Request {request_id} has arrived...")

            # 1) Check the current capacity (by using time)
            curr_time = time.time()

            drop_amount = math.floor(
                (curr_time - self.last_drop_check_time) * self.drop_rate
            )

            self.current_load = max(self.current_load - drop_amount, 0)

            self.last_drop_check_time = curr_time

            print(
                f"Before operations, load is: {self.current_load}/{self.max_capacity}"
            )

            # 2) Check if the incoming request would result in overflow
            # 3) If yes, return False
            if self.current_load == self.max_capacity:
                print(f"Request {request_id} will be rejected.")
                print()
                return False

            # 4) If no, increase the current capacity by one, return True
            if self.current_load < self.max_capacity:
                print(f"Request {request_id} will be accepted.")
                self.current_load += 1
                print()
                return True


def test_is_allowed():
    MAX_CAPACITY = 3
    DROP_RATE = 1

    leakyBucket = LeakyBucket(
        MAX_CAPACITY, DROP_RATE
    )  # Meaning that, in every 3 seconds, the bucket will be completely empty

    producer_threads = [
        threading.Thread(target=leakyBucket.is_allowed, args=(i + 1,))
        for i in range(0, 6)
    ]

    for i in range(MAX_CAPACITY):
        producer_threads[i].start()
        producer_threads[i].join()

    time.sleep(MAX_CAPACITY / DROP_RATE)

    for i in range(MAX_CAPACITY, len(producer_threads)):
        producer_threads[i].start()
        producer_threads[i].join()


test_is_allowed()
