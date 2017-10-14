#!/bin/python3
import time

# Constraints: Each side of box must be strictly larger than that of box below it. Cannot rotate boxes.

def findMaxStack(boxes):
    myStack=[-1 for b in range(len(boxes))]
    findStack_helper(0, boxes, myStack)
    return max(myStack)


def findStack_helper(box, boxes, myStack):
    if myStack[box] != -1:
        return myStack[box]
    myStack[box] = 1

    a1, a2, a3 = boxes[box]
    for b in range(len(boxes)):
        b1, b2, b3 = boxes[b]
        if b1 > a1 and b2 > a2 and b3 > a3:     # it's a valid box!
            myStack[box] = max(myStack[box], findStack_helper(b, boxes, myStack) + 1)

    return myStack[box]


def test(inp, case=1):

    print("-----TESTING BEGINS-----")
    res = findMaxStack(inp)
    print(res)
    return res



if __name__ == '__main__':

    inps = [[(1,1,1),(1,2,3),(5,4,4),(10,10,10)]]

    for inp in inps:
        start_time = time.time()
        test(inp, 1)
        t1 = time.time() - start_time
        print(t1)