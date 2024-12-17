"""
1114. Print FooBar Alternately

Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads:

thread A will call foo(), while
thread B will call bar().
Modify the given program to output "foobar" n times.

Example 1:
  Input: n = 1
  Output: "foobar"
  Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
  "foobar" is being output 1 time.


Example 2:

  Input: n = 2
  Output: "foobarfoobar"
  Explanation: "foobar" is being output 2 times.


Algorithm Implementation:


Complexities:

Tryouts:

  n = 2 -> foo bar foo bar

  foobar

"""

from typing import Callable
import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_done = threading.Event()
        self.bar_done = threading.Event()

        # Initially, we need to allow `foo` to print, so we can set the bar_done to true
        self.bar_done.set()

    def foo(self, printFoo: "Callable[[], None]") -> None:

        for i in range(self.n):
            # In order to print foo again, we need to wait for bar to be done
            self.bar_done.wait()

            printFoo()

            # Preparing for the next iteration
            # Bar needs to be cleared, because it's not printed yet
            self.bar_done.clear()

            # Foo is printed, we can set the value, so that bar could be printed
            self.foo_done.set()

    def bar(self, printBar: "Callable[[], None]") -> None:

        for i in range(self.n):

            # We need to wait until foo is printed
            self.foo_done.wait()

            # printBar() outputs "bar". Do not change or remove this line.
            printBar()

            self.foo_done.clear()
            # Bar is printed, we can set the value
            self.bar_done.set()


def printFoo():
    print("foo", end="")


def printBar():
    print("bar", end="")


n = 2
foobar = FooBar(n)

thread_foo = threading.Thread(target=foobar.foo, args=(printFoo,))
thread_bar = threading.Thread(target=foobar.bar, args=(printBar,))

thread_foo.start()
thread_bar.start()

thread_foo.join()
thread_bar.join()
print()
