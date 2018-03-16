#!usr/bin/env python3

"""
london_bridge.py
Child game
@author Dexter Renick
@version 2018-03-1
"""

from atds import Queue
from random import *

def main():
    song = ["London Bridge is falling down",
            "falling down",
            "falling down",
            "London Bridge is falling down",
            "My Fair Lady",
            "Take the key and lock her up",
            "lock her up",
            "lock her up",
            "Take the key and lock her up",
            "My Fair Lady"]

    people = ["Shaya","Chase","Dexter","Mariano",
              "Richard T","Richard W","Elizabeth",
              "Ethan","Jack W","Jack S","Paul","Aisling",
              "Brad","Harry"]
    q = Queue()

    # How to put the people into the queue in random order?
    '''
    while len(people) > 0:
        q.enqueue(people.pop(randrange(len(people))))
    '''
    shuffle(people)
    for person in people:
        q.enqueue(person)

    # Let's start playing the game
    line_counter = 0
    song_length = len(song)
    while not q.isEmpty():
        print(song[line_counter % song_length], end=' ')
        line_counter += 1
        person = q.dequeue()
        print("[" + person + "]")
        if line_counter % 5 == 0:
            if q.isEmpty():
                print(person + " wins!")
            else:
                print(person + " is out!")
        else:
            q.enqueue(person)


if __name__ == "__main__":
    main()
