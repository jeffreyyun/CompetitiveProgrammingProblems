# -*- coding: utf-8 -*-

# Problem Set 6: Simulating robots
# Name: Haoyu Yun
# Collaborators:
# Time: 2:00

from __future__ import print_function

import math
import random
import tkinter as tk
import numpy as np

import ps6_visualize
import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.room = [[0 for x in range(height)] for y in range(width)]
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.room[int(pos.getX())][int(pos.getY())] = 1;

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.room[m][n]
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width*self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return sum(map(sum,self.room))

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position(random.randrange(self.width), random.randrange(self.height))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return (0 <= pos.getX() < self.width) and (0 <= pos.getY() < self.height)


class Robot(object):
    """# -*- coding: utf-8 -*-
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.speed = speed
        self.room = room
        self.pos = room.getRandomPosition()
        self.dir = random.randrange(360)
        self.room.cleanTileAtPosition(self.pos)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.dir

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.dir = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        newpos = self.pos.getNewPosition(self.dir, self.speed)
        while not self.room.isPositionInRoom(newpos):
            self.setRobotDirection(random.randrange(360))
            newpos = self.pos.getNewPosition(self.dir, self.speed)
        self.setRobotPosition(newpos)
        self.room.cleanTileAtPosition(newpos.getX(), newpos.getY())
        return


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        newpos = self.pos.getNewPosition(self.dir, self.speed)
        if not self.room.isPositionInRoom(newpos):
            self.setRobotDirection(random.randrange(360))
        else:
            self.setRobotPosition(newpos)
            self.room.cleanTileAtPosition(newpos)

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """

    timesteps = []
    for t in range(num_trials):
        #anim = ps6_visualize.RobotVisualization(num_robots, width, height)

        room = RectangularRoom(width, height)
        robots = []
        for r in range(num_robots):
            robots.append(robot_type(room, speed))
        count = 0
        while (room.getNumCleanedTiles()/room.getNumTiles() < min_coverage):
            count += 1
            for r in robots:
                r.updatePositionAndClean()
            #anim.update(room, robots)
        #anim.done()
        timesteps.append(count)
    return np.mean(timesteps)


# === Problem 4
#
# 1) How long does it take to clean 80% of a 20×20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#	 20×20, 25×16, 40×10, 50×8, 80×5, and 100×4?

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """ 
    avgs = []
    n_robots = [x for x in range(1,10)]
    for n in n_robots:
        avgs.append(runSimulation(n,1.0,20,20,0.8,50,StandardRobot))
    pylab.plot(n_robots, avgs)
    pylab.title("Time to Clean 80% of 20x20 Room with Various Number of Robots")
    pylab.xlabel("Number of Robots")
    pylab.ylabel("Time Steps to Clean")
    pylab.show()


def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    avgs = []
    r_sizes = [20, 25, 40, 50, 80, 100]
    for n in r_sizes:
        avgs.append(runSimulation(2,1.0,n,int(400/n),0.8,50,StandardRobot))
    pylab.plot(r_sizes, avgs)
    pylab.title("Time to Clean 80% of rectangular room with 2 robots, for various room sizes")
    pylab.xlabel("Width of room with area 400")
    pylab.ylabel("Time Steps to Clean")
    pylab.show()

#showPlot1()
#showPlot2()

# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    def updatePositionAndClean(self):
        self.setRobotDirection(random.randrange(360))
        newpos = self.pos.getNewPosition(self.dir, self.speed)
        while not self.room.isPositionInRoom(newpos):
            self.setRobotDirection(random.randrange(360))
            newpos = self.pos.getNewPosition(self.dir, self.speed)
        self.setRobotPosition(newpos)
        self.room.cleanTileAtPosition(newpos)

#print(runSimulation(1, 1.0, 10, 10, 0.8, 50, RandomWalkRobot))

# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    standard_avgs = []
    rw_avgs = []
    r_sizes = [20, 25, 40, 50, 80, 100]
    for n in r_sizes:
        standard_avgs.append(runSimulation(3,1.0,n,int(400/n),0.8,50,StandardRobot))
        rw_avgs.append(runSimulation(3,1.0,n,int(400/n),0.8,50,RandomWalkRobot))
    pylab.plot(r_sizes, standard_avgs, '-b', label="standard")
    pylab.plot(r_sizes, rw_avgs, '-r', label="rw")
    pylab.title("Time to Clean 80% of rectangular room with 3 robots of different types, for various room sizes")
    pylab.xlabel("Width of room with area 400")
    pylab.ylabel("Time Steps to Clean")
    pylab.show()

showPlot3()