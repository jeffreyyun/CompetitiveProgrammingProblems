#!/bin/python3
import time

# Goal: Find height of max stack
# Constraints: Each side of box must be strictly larger than that of box below it. Cannot rotate boxes.

def findMaxStack(boxes):
    myStack=[-1 for b in range(len(boxes))]
    # sort on heights
    boxes.sort(key=lambda b: b[1])
    print(boxes)
    for i in range(len(boxes)):
        findStack_helper(i, boxes, myStack)
    return max(myStack)


def findStack_helper(box, boxes, myStack):
    if myStack[box] != -1:
        return myStack[box]
    w1, h1, d1 = boxes[box]
    myStack[box] = h1

    for b in range(len(boxes)):
        w2, h2, d2 = boxes[b]
        if d2 > d1 and w2 > w1 and h2 > h1:     # it's a valid box!
            myStack[box] = max(myStack[box], findStack_helper(b, boxes, myStack) + h1)

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