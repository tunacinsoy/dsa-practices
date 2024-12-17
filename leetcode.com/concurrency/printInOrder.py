"""
1114. Print In Order

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}

  The same instance of Foo will be passed to three different threads.
  Thread A will call first(), thread B will call second(), and thread C will call third().
  Design a mechanism and modify the program to ensure that second() is executed after first(), and
  third() is executed after second().

Note:

  We do not know how the threads will be scheduled in the operating system,
  even though the numbers in the input seem to imply the ordering.
  The input format you see is mainly to ensure our tests' comprehensiveness.

Example 1:
  Input: nums = [1,2,3]
  Output: "firstsecondthird"
  Explanation: There are three threads being fired asynchronously.
  The input [1,2,3] means thread A calls first(),
  thread B calls second(), and thread C calls third().
  "firstsecondthird" is the correct output.

Example 2:

  Input: nums = [1,3,2]
  Output: "firstsecondthird"
  Explanation: The input [1,3,2] means thread A calls first(),
  thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.


Algorithm Implementation:

  We need two different locks (event type), one for the end of first() function, the other for end of second() function.
  Thread B will wait until first_done event is set, and thread c will wait until second_done event is set.


Complexities:

"""

import threading
from typing import Callable


class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()
        self.first_done.clear()
        self.second_done.clear()
        pass

    def first(self, printFirst: "Callable[[], None]") -> None:
        printFirst()
        self.first_done.set()
        pass

    def second(self, printSecond: "Callable[[], None]") -> None:
        self.first_done.wait()
        printSecond()
        self.second_done.set()

    def third(self, printThird: "Callable[[], None]") -> None:
        self.second_done.wait()
        printThird()


def printFirst():
    print("first", end="")
    pass


def printSecond():
    print("second", end="")
    pass


def printThird():
    print("third", end="")
    pass


foo = Foo()

first_thread = threading.Thread(target=foo.first, args=(printFirst,))
second_thread = threading.Thread(target=foo.second, args=(printSecond,))
third_thread = threading.Thread(target=foo.third, args=(printThird,))

first_thread.start()
second_thread.start()
third_thread.start()

first_thread.join()
first_thread.join()
first_thread.join()
print()
