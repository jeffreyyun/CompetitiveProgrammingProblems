# 6.00 Problem Set 11
#
# ps11.py
#
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
from graph import Digraph, Edge, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Write a couple of sentences describing how you will model the
# problem as a graph)
#

# I can use adjacency lists, with each array storing a tuple of three elements


def load_map(mapFilename):
	""" 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
	# assumes no more than one edge between any two nodes
	d = Digraph()
	with open(mapFilename, 'r') as f:
		print "Loading map from file..."
		for line in f:
			edata = [x for x in line.split()]
			node1, node2 = edata[0], edata[1]
			if not d.hasNode(node1):
				d.addNode(node1)
			if not d.hasNode(node2):
				d.addNode(node2)
			e = WeightedEdge(*edata)
			d.addEdge(e)
	return d

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and the constraints
#

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors, visited=[], counter=0):    
	"""
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDisOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
	if not (digraph.hasNode(start) and digraph.hasNode(end)):
		raise ValueError('Node not valid')
	path = [str(start)]
	if start == end:
		return path
	shortest = None		# to append to path
	visited = visited + [str(start)]
	for node in digraph.childrenOf(start).keys():		# visits each node

		if (str(node) not in visited):					# if new, unvisited node
			visited = visited + [str(node)]
			dist, out = digraph.childrenOf(start)[node]
			new_mTD = maxTotalDist - int(dist)
			new_mDO = maxDistOutdoors - int(out)

			if (new_mTD < 0 or new_mDO < 0):
				visited.remove(str(node))
				continue

			# try the path
			newPath = bruteForceSearch(digraph, node, end, new_mTD, new_mDO, visited, counter=counter + 1)
			if newPath == None:
				continue
			if (shortest == None or digraph.getLength(newPath) < digraph.getLength(shortest)):
				# stores total distance left
				shortest = newPath			

	if shortest != None:
		return path + shortest
	else:
		if counter == 0:
			raise ValueError('No such path exists!')
		return None


#
# Problem 4: Finding the Shortest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors, visited=[], memo={}, counter=0):
	"""
	Finds the shortest path from start to end using directed depth-first.
	search approach. The total distance travelled on the path must not
	exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDisOutdoors.

	Parameters: 
	    digraph: instance of class Digraph or its subclass
	    start, end: start & end building numbers (strings)
	    maxTotalDist : maximum total distance on a path (integer)
	    maxDistOutdoors: maximum distance spent outdoors on a path (integer)

	Assumes:
	    start and end are numbers for existing buildings in graph

	Returns:
	    The shortest-path from start to end, represented by 
	    a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
	    where there exists an edge from n_i to n_(i+1) in digraph, 
	    for all 1 <= i < k.

	    If there exists no path that satisfies maxTotalDist and
	    maxDistOutdoors constraints, then raises a ValueError.
	"""
	if not (digraph.hasNode(start) and digraph.hasNode(end)):	# if not in graph
		raise ValueError('Start or end not in graph.')
	path = [str(start)]										# path from start to end
	if start == end:										# path consists only of dest
		return path
	shortest = None
	visited = visited + [str(start)]						# makes sure start is in visited

	for node in digraph.childrenOf(start).keys():			# for each neighbor to this node
		if (str(node) not in visited):						# if not already visited
			visited = visited + [str(node)]					# mark as visited
			dist, out = digraph.childrenOf(start)[node]		# gets distanceTotal and distanceOutside
			new_mTD = maxTotalDist - int(dist)
			new_mDO = maxDistOutdoors - int(out)

			if (new_mTD < 0 or new_mDO < 0):				# would violate constraints if we go here next, so skip to next one
				visited.remove(str(node))					# unmark as visited
				continue

			try:
				del(memo[node, end])
			except:
				pass

			try:
				newPath = memo[node, end]					# if path exists in memo, use that paths		# Problem: not getting the optimal path saved....!!!
			except:
				newPath = directedDFS(digraph, node, end,		# if does not exist, find a new path
					new_mTD, new_mDO,
					visited, memo, counter=counter+1)

			if newPath == None:								# if no path found
				continue

			if (shortest == None or digraph.getLength(newPath) < digraph.getLength(shortest)):	# if this path is better than the previous
				shortest = newPath							# sets shortest discovered path to newPath
				memo[node, end]= newPath					# saves this optimal path into memo

	if (shortest != None):
		return path + shortest 								# extends the path
	else:
		if counter == 0:
			raise ValueError('No such path exists!')		
		return None											# no forward path meeting the constraints found




# Uncomment below when ready to test
if __name__ == '__main__':
   # Test cases
   digraph = load_map("mit_map.txt")

   LARGE_DIST = 1000000

   # Test case 1
   print "---------------"
   print "Test case 1:"
   print "Find the shortest-path from Building 32 to 56"
   expectedPath1 = ['32', '56']
   brutePath1 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
   dfsPath1 = directedDFS(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
   print "Expected: ", expectedPath1
   print "Brute-force: ", brutePath1
   print "DFS: ", dfsPath1

   #Test case 2
   print "---------------"
   print "Test case 2:"
   print "Find the shortest-path from Building 32 to 56 without going outdoors"
   expectedPath2 = ['32', '36', '26', '16', '56']
   brutePath2 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, 0)
   dfsPath2 = directedDFS(digraph, '32', '56', LARGE_DIST, 0)
   print "Expected: ", expectedPath2
   print "Brute-force: ", brutePath2
   print "DFS: ", dfsPath2

   # Test case 3
   print "---------------"
   print "Test case 3:"
   print "Find the shortest-path from Building 2 to 9"
   expectedPath3 = ['2', '3', '7', '9']
   brutePath3 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
   dfsPath3 = directedDFS(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
   print "Expected: ", expectedPath3
   print "Brute-force: ", brutePath3
   print "DFS: ", dfsPath3

   # Test case 4
   print "---------------"
   print "Test case 4:"
   print "Find the shortest-path from Building 2 to 9 without going outdoors"
   expectedPath4 = ['2', '4', '10', '13', '9']
   brutePath4 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, 0)
   dfsPath4 = directedDFS(digraph, '2', '9', LARGE_DIST, 0)
   print "Expected: ", expectedPath4
   print "Brute-force: ", brutePath4
   print "DFS: ", dfsPath4

   # Test case 5
   print "---------------"
   print "Test case 5:"
   print "Find the shortest-path from Building 1 to 32"
   expectedPath5 = ['1', '4', '12', '32']
   brutePath5 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
   dfsPath5 = directedDFS(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
   print "Expected: ", expectedPath5
   print "Brute-force: ", brutePath5
   print "DFS: ", dfsPath5

   # Test case 6
   print "---------------"
   print "Test case 6:"
   print "Find the shortest-path from Building 1 to 32 without going outdoors"
   expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
   brutePath6 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, 0)
   dfsPath6 = directedDFS(digraph, '1', '32', LARGE_DIST, 0)
   print "Expected: ", expectedPath6
   print "Brute-force: ", brutePath6
   print "DFS: ", dfsPath6

   # Test case 7
   print "---------------"
   print "Test case 7:"
   print "Find the shortest-path from Building 8 to 50 without going outdoors"
   bruteRaisedErr = 'No'
   dfsRaisedErr = 'No'
   try:
       bruteForceSearch(digraph, '8', '50', LARGE_DIST, 0)
   except ValueError:
       bruteRaisedErr = 'Yes'
   
   try:
       directedDFS(digraph, '8', '50', LARGE_DIST, 0)
   except ValueError:
       dfsRaisedErr = 'Yes'
   
   print "Expected: No such path! Should throw a value error."
   print "Did brute force search raise an error?", bruteRaisedErr
   print "Did DFS search raise an error?", dfsRaisedErr

   # Test case 8
   print "---------------"
   print "Test case 8:"
   print "Find the shortest-path from Building 10 to 32 without walking"
   print "more than 100 meters in total"
   bruteRaisedErr = 'No'
   dfsRaisedErr = 'No'
   try:
       bruteForceSearch(digraph, '10', '32', 100, LARGE_DIST)
   except ValueError:
       bruteRaisedErr = 'Yes'
   
   try:
       directedDFS(digraph, '10', '32', 100, LARGE_DIST)
   except ValueError:
       dfsRaisedErr = 'Yes'
   
   print "Expected: No such path! Should throw a value error."
   print "Did brute force search raise an error?", bruteRaisedErr
   print "Did DFS search raise an error?", dfsRaisedErr

