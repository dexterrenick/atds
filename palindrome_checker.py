#!usr/bin/env python3

"""
palindrome.py
Tests if two words are palindrome of each other
@author Dexter Renick
@version 2018-05-18
"""


from atds import Deque

def palchecker(expression):
    d = Deque()

    for letter in expression:
        d.addRear(letter)
    stillEqual = True
    while d.size() > 1 and stillEqual:
        first = d.removeFront()
        last = d.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print("Testing the expression hannah:", palchecker("hannah"))
print("Testing the expression kjladf;jklas;fjkdlas;jkl:", palchecker("kjladf;jklas;fjkdlas;jkl"))
