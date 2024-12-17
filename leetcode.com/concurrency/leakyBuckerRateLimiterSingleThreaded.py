"""
Description:

    Implement a rate limiter using leaky bucket algorithm. First, design with single-thread, and then convert the code into multithreaded.


Algorithm Implementation:
    Leaky Bucket has constant capacity, and constant drop rate.


"""

import time
import math


class LeakyBucket:
    def __init__(self, capacity: int, drop_rate: float):
        self.capacity = capacity
        # In terms of second -> 5 requests per second, 2 requests per second etc.
        self.drop_rate = drop_rate
        self.last_drop_check_time = time.time()
        self.current_capacity = 0

    def is_allowed(self, request_id: int):

        print(f"Request {request_id} has arrived...")

        # 1) Check the current capacity (by using time)
        curr_time = time.time()

        drop_amount = math.floor(
            (curr_time - self.last_drop_check_time) * self.drop_rate
        )

        print(drop_amount)

        # self.current_capacity = math.ceil(max(self.current_capacity - drop_amount, 0))

        self.current_capacity = max(self.current_capacity - drop_amount, 0)

        self.last_drop_check_time = curr_time

        print(
            f"Before operations, capacity is: {self.current_capacity}/{self.capacity}"
        )

        # 2) Check if the incoming request would result in overflow
        # 3) If yes, return False
        if self.current_capacity == self.capacity:
            print(f"Request {request_id} will be rejected.")
            print()
            return False

        # 4) If no, increase the current capacity by one, return True
        if self.current_capacity < self.capacity:
            print(f"Request {request_id} will be accepted.")
            self.current_capacity += 1
            print()
            return True


def test_is_allowed():

    MAX_CAPACITY = 3
    DROP_RATE = 0.25

    leakyBucket = LeakyBucket(
        MAX_CAPACITY, DROP_RATE
    )  # Meaning that, in every 4 seconds, bucket will leak 1 drop

    assert leakyBucket.is_allowed(1) == True
    assert leakyBucket.is_allowed(2) == True
    assert leakyBucket.is_allowed(3) == True

    assert leakyBucket.is_allowed(4) == False  # this has to be rejected

    print(f"We will wait for {MAX_CAPACITY / DROP_RATE} seconds...")
    time.sleep(MAX_CAPACITY / DROP_RATE)  # emptying the bucket

    assert leakyBucket.is_allowed(5) == True
    assert leakyBucket.is_allowed(6) == True
    assert leakyBucket.is_allowed(7) == True

    print(f"We will wait for {1 / DROP_RATE} seconds...")
    time.sleep(1 / DROP_RATE)
    assert leakyBucket.is_allowed(8) == True  # this has to be accepted

    print("All tests passed!")


test_is_allowed()
