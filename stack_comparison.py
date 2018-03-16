#!/usr/bin/env python3
"""
stack_comparison.py
Program that compares UnorderedList and UnorderedListStack
@author Dexter Renick
@version 2018-27-2
"""
"""
Program Operations:
This program pushes and pops a list created using the Stack and UnorderedListStack
Classes with the numbers from one to 1, 10,100,1000, and 10000. The program then determines,
based on individual completion speed, which class is however many times faster for operations.

Results:
Stack and UnorderedListStack pushed the items with similar
speeds with Stack consistently finishing a bit faster.
1-1: 1.50 times faster (Stack won)
1-10: 1.24 times faster (Stack won)
1-100: 2.49 times faster (Stack won)
1-1000: 2.88 times faster (Stack won)
1-10000: 4.99 times faster (Stack won)

Stack and UnorderedListStack popped the items with similar
speeds with Stack consistently finishing a bit faster.
1-1: 1.40 times faster (Stack won)
1-10: 1.76 times faster (Stack won)
1-100: 2.00 times faster (Stack won)
1-1000: 2.31 times faster (Stack won)
1-10000: 2.80 times faster (Stack won)

Analysis:
Stack is a class in python, it adds an item to the end of the list, equivalent to a[len(a):] = [x],
and pop simply removes the last item in the list(if not otherwise specified). UnorderedListStack implements UnorderedList,
which implements Node to create a linked list of data; furthermore, the add is adding the item
to the left side of the list (the back) and then pop removes the furthest to the left item of the list (the back).
The reason that the left side of the list is the back, is that if the right side was the back, which may visually
be more pleasing, would make the program much less effecient because to add and pop items the entire list of items
would need to be read through.

Based on the tests, in both push and pop stack, python's class (interpreted with Stack), is faster and increases linearly
with input data size. The reason for UnorderedListStack stacks slower times, is due to the fact that it needs to call
more functions from other classes as well as preform more operations, but overall it is fairly efficient for a linked list.
"""

from atds import *
import time

def main():
    stack = Stack()
    ulstack = UnorderedListStack()
    n = 1
    while n < 100000:
        print("Testing UnorderedList and UnorderedListStack push speed with numbers 1 -",n)
        start = time.time()
        for i in range((n)):
            stack.push(i)
        stop = time.time()
        pushtest1 = (stop-start)
        print(pushtest1)
        start = time.time()
        for i in range((n)):
            ulstack.push(i)
        stop = time.time()
        pushtest2 = (stop-start)
        print(pushtest2)
        print()
        if pushtest2>pushtest1:
            print("Stack pushed", pushtest2/pushtest1,"times faster")

        else:
            print("UnorderedListStack pushed",pushtest1/pushtest2,"times faster")

        print()
        print("Testing Stack and UnorderedListStack pop speed(with numbers 1 -",n)
        start = time.time()
        while stack.isEmpty() == False:
            stack.pop()
        stop = time.time()
        poptest1 = (stop-start)
        print(poptest1)
        start = time.time()
        while ulstack.isEmpty() == False:
            ulstack.pop()
        stop = time.time()
        poptest2 = (stop-start)
        print(poptest2)
        print()
        if poptest2>poptest1:
            print("Stack popped", poptest2/poptest1,"times faster")
        else:
            print("UnorderedListStack popped",pushtest1/pushtest2,"times faster")
        print()
        n = n*10


if __name__ == '__main__':
    main()
