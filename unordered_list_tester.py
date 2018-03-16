#!/usr/bin/env python3
"""
UnorderedListTester.py
This UnorderedList Tester creates an UnorderedList object based
on your class description, and tests to see if it can handle
the common methods.

Your UnorderedList class, and the Node class that it uses, should
be defined in your atds module. In order to assist you in
debugging any errors, make sure you use the following __repr__
method in your UnorderedList. This will allow you to see what's
happening in your list, and will allow the Tester to provide
better diagnostics for your debugging pleasure. :)

    def __repr__(self):
        '''Creates a representation of the list suitable for
        printing, debugging.
        '''
        returnValue = "UnorderedList["
        nextNode = self.head
        while nextNode != None:
            returnValue += str(nextNode.getData()) + ","
            nextNode = nextNode.getNext()
        if returnValue[-1] == ",":
            returnValue = returnValue[:-1] # remove trailing comma
        returnValue = returnValue + "]"
        return returnValue

@author Richard White
@version 2017-03-14
"""

from atds import *          # Uses the UnorderedList and Node classes

def main():
    print("Testing the UnorderedList class")
    testsPassed = 0
    try:
        ul = UnorderedList()
        testsPassed += 1
        print("Test passed: UnorderedList object created")
    except:
        print("Test failed: couldn't create UnorderedList object")

    try:
        if ul.isEmpty():
            testsPassed += 1
            print("Test passed: .isEmpty() method detected empty list")
        else:
            print("Test failed: .isEmpty() method didn't understand that list is empty")
    except:
        print("Test failed: .isEmpty method unavailable")

    try:
        if ul.length() == 0:
            testsPassed += 1
            print("Test passed: .length() correctly identified a length of 0")
        else:
            print("Test failed: .length() didn't identify a length of 0")
    except:
        print("Test failed: .length() method unavailable")

    try:
        ul.add(4)
        ul.add(3)
        ul.add(2)
        ul.add(1)
        ul.add(0)
        testsPassed += 1
        print("Test passed: five items added")
    except:
        print("Test failed: couldn't add items")

    try:
        if not ul.isEmpty():
            testsPassed += 1
            print("Test passed: .isEmpty() method identified that list is no longer empty")
        else:
            print("Test failed: .isEmpty() method thought list was empty, and it isn't")
    except:
        print("Test failed: .isEmpty method unavailable")

    try:
        if ul.length() == 5:
            testsPassed += 1
            print("Test passed: .length() correctly identified a length of 5")
        else:
            print("Test failed: .length() didn't identify a length of 5")
    except:
        print("Test failed: .length() method unusable")

    try:
        result = str(ul)         # Try using __repr__
        if result == "UnorderedList[0,1,2,3,4]":
            testsPassed += 1
            print("Test passed: __repr__ returning correct values:")
            print(result)
        else:
            print("Test failed: __repr__ returned " + result)
            print("Expected: UnorderedList[0,1,2,3,4]")

    except:
        print("Test failed: couldn't reference __repr__ method")



    try:
        if not ul.search(5):
            testsPassed += 1
            print("Test passed: .search() method correctly identified that 5 isn't on list")
        else:
            print("Test failed: .search() method thought 5 is on list when it isn't")
    except:
        print("Test failed: .search() method unavailable")

    try:
        if ul.search(3):
            testsPassed += 1
            print("Test passed: .search() method correctly identified that 3 is on list")
        else:
            print("Test failed: .search() method thought 3 is on list when it isn't")
    except:
        print("Test failed: .search() method unavailable")

    try:
        ul.remove(0)
        if str(ul) == "UnorderedList[1,2,3,4]":
            testsPassed += 1
            print("Test passed: .remove() successfully removed item from beginning of list")
        else:
            print("Test failed: .remove() didn't remove item from beginning of list")
    except:
        print("Test failed: .remove() method unavailable? (or __repr__ not working?)")

    try:
        ul.remove(2)
        if str(ul) == "UnorderedList[1,3,4]":
            testsPassed += 1
            print("Test passed: .remove() successfully removed item from middle of list")
        else:
            print("Test failed: .remove() didn't remove item from middle of list")
    except:
        print("Test failed: .remove() method unavailable? (or __repr__ not working?)")

    try:
        ul.remove(4)
        if str(ul) == "UnorderedList[1,3]":
            testsPassed += 1
            print("Test passed: .remove() successfully removed item from end of list")
        else:
            print("Test failed: .remove() didn't remove item from end of list")
    except:
        print("Test failed: .remove() method unavailable? (or __repr__ not working?)")

    try:
        print("Attempting multiple remove")
        ul.add(1)
        print("Before remove: " + str(ul))
        ul.remove(1)
        print("After remove: " + str(ul))
        result = ul.search(1)
        if not result:
            testsPassed += 1
            print("Test passed: .remove() successfully removed multiple items")
        else:
            print("Test failed: .remove() didn't remove multiple items")
    except:
        print("Test failed: .remove() method unavailable? (or __repr__ not working?)")

    try:
        ul.append(4)
        if str(ul) == "UnorderedList[3,4]":
            testsPassed += 1
            print("Test passed: .append() successfully appended item to list")
        else:
            print("Test failed: .append() didn't append time to list")
    except:
        print("Test failed: .append() method unavailable? (or __repr__ not working?)")

    try:
        result = ul.index(4)
        if result == 1:
            testsPassed += 1
            print("Test passed: .index() successfully found item on list")
        else:
            print("Test failed: .index() failed to find item on list")
    except:
        print("Test failed: .index() method unavailable? (or __repr__ not working?)")

    try:
        ul.insert(1, 2)
        ul.insert(0,1)
        if str(ul) == "UnorderedList[1,3,2,4]":
            testsPassed += 1
            print("Test passed: .insert() successfully inserted values on list")
        else:
            print("Test failed: .insert() didn't insert values correctly")
    except:
        print("Test failed: .insert() method unavailable? (or __repr__ not working?)")

    try:
        ul.pop()
        if str(ul) == "UnorderedList[1,3,2]":
            testsPassed += 1
            print("Test passed: .pop() successfully removed last item from list")
        else:
            print("Test failed: .pop() didn't remove last item from list correctly")
    except:
        print("Test failed: .pop() method unavailable? (or __repr__ not working?)")
    
    try:
        ul.pop(1)
        if str(ul) == "UnorderedList[1,2]":
            testsPassed += 1
            print("Test passed: .pop() successfully removed last item from list")
        else:
            print("Test failed: .pop() didn't remove last item from list correctly")
    except:
        print("Test failed: .pop() method unavailable? (or __repr__ not working?)")

    print(str(testsPassed) + "/18 tests passed on the UnorderedList class")


if __name__ == "__main__":
    main()
