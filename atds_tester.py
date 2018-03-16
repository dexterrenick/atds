#!usr/bin/env python3

"""
atds_tester.py
Runs a series of tests on the atds module, including looking at
    * Stack
    * Queue
    * Deque
@author Richard White
@version 2017-03-13
"""

from atds import *

def main():

#################################################################

    print("Testing the Stack class")
    testsPassed = 0
    try:
        s = Stack()
        testsPassed += 1
        print("Test passed: stack created")
    except:
        print("Test failed: couldn't initialize stack")

    try:
        s.push("hello")
        s.push(3)
        testsPassed += 1
        print("Test passed: items pushed")
    except:
        print("Test failed: couldn't push onto stack")

    try:
        result = s.peek()
        if (result == 3):
            testsPassed += 1
            print("Test passed: peeked at item")
        else:
            print("Test failed: incorrect peek value")
    except:
        print("Test failed: couldn't peek at stack")

    try:
        result = s.pop()
        if (result == 3):
            testsPassed += 1
            print("Test passed: item popped")
        else:
            print("Test failed: incorrect pop result")
    except:
        print("Test failed: couldn't pop")

    try:
        result = s.isEmpty()
        if (not result):
            testsPassed += 1
            print("Test passed: isEmpty returned correct result")
        else:
            print("Test failed: stack has items, but indicated empty")
    except:
        print("Test failed: isEmpty() method unavailable")

    try:
        result = s.size()
        if (result == 1):
            testsPassed += 1
            print("Test passed: correct size returned")
        else:
            print("Test failed: incorrect size returned")
    except:
        print("Test failed: .size() method unavailable")

    try:
        s.pop()
    except:
        pass

    try:
        result = s.isEmpty()
        if (result):
            testsPassed += 1
            print("Test passed: .isEmpty() correctly indicating empty status")
        else:
            print("Test failed: stack failed to indicate empty status")
    except:
        print("Test failed: isEmpty() unavailable")

    print(str(testsPassed) + "/7 tests passed on the Stack class")

#################################################################

    print("Testing the Queue class")
    testsPassed = 0
    try:
        q = Queue()
        testsPassed += 1
        print("Test passed: queue created")
    except:
        print("Test failed: couldn't initialize queue")

    try:
        q.enqueue(5)
        q.enqueue(7)
        testsPassed += 1
        print("Test passed: items enqueued")
    except:
        print("Test failed: couldn't enqueue onto queue")

    try:
        result = q.dequeue()
        if (result == 5):
            testsPassed += 1
            print("Test passed: dequeued correct value")
        else:
            print("Test failed: incorrect value dequeued")
    except:
        print("Test failed: couldn't dequeue")

    try:
        result = q.size()
        if (result == 1):
            testsPassed += 1
            print("Test passed: correct size returned")
        else:
            print("Test failed: incorrect size returned")
    except:
        print("Test failed: .size() method unavailable")

    try:
        result = q.isEmpty()
        if (not result):
            testsPassed += 1
            print("Test passed: isEmpty correctly returned false on queue")
        else:
            print("Test failed: queue has items, but indicated empty")
    except:
        print("Test failed: isEmpty() method unavailable")

    try:
        tmp = q.dequeue() # just emptying the queue
        result = q.isEmpty()
        if (result):
            testsPassed += 1
            print("Test passed: .isEmpty() correctly indicating empty status")
        else:
            print("Test failed: queue failed to indicate empty status")
    except:
        print("Test failed: isEmpty() unavailable")

    print(str(testsPassed) + "/6 tests passed on the Queue class")

#################################################################

    print("Testing the Deque class")
    testsPassed = 0
    try:
        d = Deque()
        testsPassed += 1
        print("Test passed: deque created")
    except:
        print("Test failed: couldn't initialize deque")

    try:
        d.addFront(1)
        d.addFront(0)
        testsPassed += 1
        print("Test passed: items added to front")
    except:
        print("Test failed: couldn't add to front")

    try:
        d.addRear(2)
        d.addRear(3)
        print("Test passed: items added to rear")
    except:
        print("Test failed: couldn't add to rear")

    try:
        result = d.removeFront()
        if result == 0:
            testsPassed += 1
            print("Test passed: removeFront retrieved correct value")
        else:
            print("Test failed: incorrect value removeFronted")
    except:
        print("Test failed: couldn't use removeFront method")

    try:
        result = d.removeRear()
        if (result == 3):
            testsPassed += 1
            print("Test passed: correct value removed from rear")
        else:
            print("Test failed: incorrect value removed from rear")
    except:
        print("Test failed: .removeRear() method unavailable")

    try:
        result = d.isEmpty()
        if (not result):
            testsPassed += 1
            print("Test passed: isEmpty correctly returned false on deque")
        else:
            print("Test failed: deque has items, but indicated empty")
    except:
        print("Test failed: isEmpty() method unavailable")

    try:
        if d.size() == 2:
            testsPassed += 1
            print("Test passed: size() returned correct value")
        else:
            print("Test failed: size() return incorrect value")
    except:
        print("Test failed: size() unavailable")

    try:
        tmp = d.removeFront()
        tmp = d.removeFront()
        result = d.isEmpty()
        if (result):
            testsPassed += 1
            print("Test passed: isEmpty correctly returned True on deque")
        else:
            print("Test failed: deque empty, but indicated notEmpty")
    except:
        print("Test failed: isEmpty() method unavailable")

    print(str(testsPassed) + "/7 tests passed on the Deque class")


if __name__ == "__main__":
    main()
