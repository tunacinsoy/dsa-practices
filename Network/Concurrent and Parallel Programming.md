
---
**Q) Example Multithreading Problems**
1. **Producer-Consumer Problem**:
    - Implement a multithreaded program where producer threads generate data and put it into a shared buffer, and consumer threads process the data.
    - Use threading locks or semaphores to manage access to the shared buffer.
2. **Thread-safe Data Structures**:
    - Create a custom thread-safe data structure, like a stack or queue, without using built-in thread-safe classes.
    - Implement synchronization to ensure data integrity during concurrent access.
3. **Multithreaded File Processing**:
    - Write a program that reads and processes multiple files concurrently.
    - For example, count word frequencies across multiple text files using multiple threads.
4. **Simple Web Crawler**:
    - Develop a multithreaded web crawler that fetches pages from a list of URLs concurrently.
    - Handle issues like avoiding duplicate downloads and managing thread lifecycles.
5. **Parallel Computation Task**:
    - Implement a computationally intensive task (e.g., calculating factorials or Fibonacci numbers) using multiple threads or processes to improve performance.
    - Use the `multiprocessing` module for CPU-bound tasks to bypass the Global Interpreter Lock (GIL).
6. **Client-Server Application**:
    - Build a simple client-server application using sockets where the server can handle multiple clients concurrently.
    - Utilize threading to manage multiple client connections.

---
**Q) Multithreading vs. Multiprocessing**
1. **I/O-Bound Tasks**: Use **multithreading** for tasks that spend most of their time waiting for external operations (e.g., network requests, file I/O).
2. **CPU-Bound Tasks**: Use **multiprocessing** for tasks that require significant CPU computation and can benefit from parallel execution across multiple cores.
3. **Mixed Workloads:** Consider using a **combination** of both approaches or asynchronous programming for complex applications with varied task types.
4. **Memory Constraints**: If memory usage is a concern, **multithreading** may be preferable due to **shared memory space**.
5. **Simplicity**: For simpler applications, **multithreading** might be easier to implement and debug.
---
**Q) What is main thread?**
The main thread is the initial thread of execution that starts when a Python program begins. It is the thread in which the main part of your program runs. When you create new threads, they run concurrently with the main thread.

The `join()` method is used to ensure that the main thread waits for all the worker threads to complete their tasks before it finishes its own execution. Without the `join()` calls, the main thread could finish and exit the program while the worker threads are still running. By using `join()`, you ensure that the main thread remains active until all the worker threads have completed their execution.

Refer: github.com/tunacinsoy/mastering-python-software-development/blob/main/ch07-concurrentAndParallelProgramming/usingThreadClass.py

---
**Q) What is mutex?**

A **mutex** (short for _mutual exclusion_) is a synchronization mechanism used in programming to control access to a shared resource in a multi-threaded or concurrent environment. It ensures that only one thread or process can access the critical section of code or the shared resource at a time, preventing data corruption or race conditions

Refer: github.com/tunacinsoy/mastering-python-software-development/blob/main/ch07-concurrentAndParallelProgramming/lock.py

We can think of a mutex as a "key" to a single-person restroom:

- If the restroom is locked, only one person can use it at a time (the person with the key).
- Others must wait outside until the keyholder exits and unlocks the door.

---
**Q) What is rlock?**

An **RLock** (short for _reentrant lock_) is a special kind of lock in Python that allows a thread to acquire the same lock multiple times without causing a deadlock.

Reference: github.com/tunacinsoy/mastering-python-software-development/blob/main/ch07-concurrentAndParallelProgramming/rlock.py

 **Use Cases for RLock:**
- Recursive functions needing a lock.
- Code where a function or method indirectly calls another function or method that also requires the lock.
- Situations requiring multiple lock acquisitions by the same thread.

---
**Q) What is Condition?**

Condition class is implemented when we have an architecture that is like producer-consumer. In this architecture, consumer threads need to wait until there's an item in the queue, and if there is not, they transform into idle state, waiting to be waken up by one of the producer threads.

Reference: github.com/tunacinsoy/mastering-python-software-development/blob/main/ch07-concurrentAndParallelProgramming/producerConsumer.py

---
**Q) What is Event?**

Event class is instantiated when there's a need for threads to act based upon an internal flag that can be set as True or False. The threads that are waiting flag to be set as true will be resume when the flag is set as true by other thread.

Reference: github.com/tunacinsoy/mastering-python-software-development/blob/main/ch07-concurrentAndParallelProgramming/event.py

---
**Q) What is Semaphore?**

Semaphore class is implemented when we want to allow a certain number of threads to be executed concurrently. It has an internal counter that is increased when a thread acquires semaphore; and decreased when a thread releases the lock.

Reference: github.com/tunacinsoy/mastering-python-software-development/blob/main/ch07-concurrentAndParallelProgramming/semaphore.py

---


Implement a fronted of a To Do List app, given a set of requirements and a simple backend server

[Answer question](https://www.glassdoor.com/Interview/Implement-a-fronted-of-a-To-Do-List-app-given-a-set-of-requirements-and-a-simple-backend-server-QTN_7627621.htm)

Question 2

Describe what happens when a user enters a web address in the browser and presses enter

[1 Answer](https://www.glassdoor.com/Interview/Describe-what-happens-when-a-user-enters-a-web-address-in-the-browser-and-presses-enter-QTN_7627622.htm)

Question 3

Describe most important HTTP methods and headers

[Answer question](https://www.glassdoor.com/Interview/Describe-most-important-HTTP-methods-and-headers-QTN_7627623.htm)

Question 4

Implementing a simple event emitter in pure JS

[Answer question](https://www.glassdoor.com/Interview/Implementing-a-simple-event-emitter-in-pure-JS-QTN_7627624.htm)

Question 5

Implementing a drop-down in pure JS according to the requirements

Interview questions [2]

Question 1

Implement TODO list in a selected technology.

[1 Answer](https://www.glassdoor.com/Interview/Implement-TODO-list-in-a-selected-technology-QTN_5801238.htm)

Question 2

Implement dropdown selection list in a selected technology.

[  
](https://www.glassdoor.com/Interview/Implement-dropdown-selection-list-in-a-selected-technology-QTN_5801239.htm)


In culture interview I’ve been asked if I had a situation when I take an initiative to introduce some innovations or how do I solve interpersonal problems

Interview questions [1]

Question 1

Tell me about handshake protocol


Interview questions [4]

Question 1

How do you find a specific log in a server file without downloading logs?

[1 Answer](https://www.glassdoor.com/Interview/How-do-you-find-a-specific-log-in-a-server-file-without-downloading-logs-QTN_7753437.htm)

Question 2

Flip a bit in an integer

[1 Answer](https://www.glassdoor.com/Interview/Flip-a-bit-in-an-integer-QTN_7753438.htm)

Question 3

Given a code that contains synchronized keyword identify issues

[1 Answer](https://www.glassdoor.com/Interview/Given-a-code-that-contains-synchronized-keyword-identify-issues-QTN_7753439.htm)

Question 4

Given a file system contains subdirectories and files, find TOP K words

Interview questions [1]

Question 1

Tell me about a difficult problem you had to solve?

Interview questions [1]

Question 1

Tell us about a project you've worked on.

Interview questions [3]

Question 1

Count the number of '1s' in an unsigned integer binary.

[2 Answers](https://www.glassdoor.com/Interview/Count-the-number-of-1s-in-an-unsigned-integer-binary-QTN_5097348.htm)

Question 2

Implement a function to get the number of visits a page got, asynchronously.

[1 Answer](https://www.glassdoor.com/Interview/Implement-a-function-to-get-the-number-of-visits-a-page-got-asynchronously-QTN_5097349.htm)

Question 3

Implement a folder directory traversal to get the minimum integer value out of all entries written in the files within these folders.

Interview questions [1]

Question 1

How to sort through log files

Basic questions like why box? describe your projects



Interview

1. Design an elevator 2. Find potential multithreading issue with two separate threads running path. 3. String parsing

Interview questions [1]

Question 1

Design an elevator control system. You need to both design the big picture and the detail scheduling algorithm.

Interview questions [1]

Question 1

What's the difference between HTTP POST and GET