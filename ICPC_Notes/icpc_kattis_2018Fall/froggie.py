# Problem D: Froggie
DEBUG = False

def calculateSafety(cx, cy, L, W, row, t):
    # Calculate position of cars in pre-move timestep (t=m)
    t %= row.interval
    offset = (row.offset+row.speed*t)%W
    interval, speed = row.interval, row.speed
    if speed >= interval:
        if DEBUG: print("Impossible to pass this lane!")
        return False
    first_car = offset-(offset//interval*interval)
    curr = list(range(first_car, W, interval))
    if DEBUG: print("prev timestamp this row was", curr, "at time", t)

    # if moving to left, flip froggie position
    if cy % 2 == 1:
        cx = W - cx - 1
        if DEBUG: print("R->L row: froggie at", (cx, cy))
    
    # Incoming car to left? Check if incoming car squishes.
    incoming_pos = (curr[0]+speed-interval)%W   # check if incoming car
    if curr[0] < cx and curr[0]+speed >= cx:    # check first car first
        if DEBUG: print("Death: firstcar moved from {} to {}".format(curr[0], curr[0]+speed))
        return False
    elif incoming_pos < curr[0]:
        incoming_pos = (curr[0]+speed-interval)%W
        res = incoming_pos < cx 
        if DEBUG:
            if not res: print("Death: incoming car to {}".format(incoming_pos))
            else: print("safe: incoming_pos is", incoming_pos)
        return res
    elif curr[0]+speed > cx:    # all cars will be to froggie's right
        return True

    leftcar = curr[0]
    # Search for car for immediate left and check if squishes.
    for i, pos in enumerate(curr):
        if pos >= cx:
            leftcar = curr[i-1]
            break
    
    leftcar_newpos = (leftcar+speed)%W
    res = leftcar_newpos < cx
    if DEBUG:
        if not res: print("Death: leftcar moved from {} to {}".format(leftcar, leftcar_newpos))
        else: print("safe: leftcar moved from {} to {}".format(leftcar, leftcar_newpos))
    return res


def simulate(board, start, moves, L, W):
    cx, cy = start, L
    dmove = {'U': (0,-1), 'D': (0,1), 'L': (-1,0), 'R': (1,0)}
    if DEBUG: print("START:", (cx, cy))
    for i, m in enumerate(moves):
        dx, dy = dmove[m]
        cx, cy = cx+dx, cy+dy
        if DEBUG: print("Checking move to", (cx, cy))
        if cy == L or cy < 0:         # moving around home row
            continue
        safe = calculateSafety(cx, cy, L, W, board[cy], i)
        if DEBUG: print("Moving to {} is safe? {}".format((cx, cy), safe))
        if not safe:        # squished
            return "squish"
    if cy < 0:       # make it to the top
        return "safe"
    else:
        # Did not make it to top
        if DEBUG: print("Ended at", (cx, cy))
        return "squish"


def initialize(W, offset, interval):
    """ Initialize starting row of cars """
    cars = [i for i in range(offset, W, interval)]
    return cars

class Row:
    def __init__(self, W, offset, interval, speed):
        self.speed = speed
        self.offset = offset
        self.interval = interval
        self.original = initialize(W, offset, interval)

L, W = map(int, input().split())
board = []
for i in range(L):
    offset, interval, speed = map(int, input().split())
    row = Row(W, offset, interval, speed)
    board.append(row)
start, moves = input().split()
start = int(start)
result = simulate(board, start, moves, L, W)
print(result)