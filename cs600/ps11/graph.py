# 6.00 Problem Set 11
#
# graph.py
#
# A set of data structures to represent graphs
#

class Node(object):
   def __init__(self, name):
       self.name = str(name)
   def getName(self):
       return self.name
   def __str__(self):
       return self.name
   def __repr__(self):
      return self.name
   def __eq__(self, other):
      return self.name == other.name
   def __ne__(self, other):
      return not self.__eq__(other)

class Edge(object):
   def __init__(self, src, dest):
       self.src = src
       self.dest = dest
   def getSource(self):
       return self.src
   def getDestination(self):
       return self.dest
   def __str__(self):
       return str(self.src) + '->' + str(self.dest)

# Problem 1:
# I simply chose to store the weights as variables 
# In this approach, the graph's nodes continue to represent locations in MIT
# The edges represent a connection between some src and dest, with weights representing
# distance between them and the time spent outside
# Digraph edges is a set of dicts of tuples
class WeightedEdge(Edge):
  def __init__(self, src, dest, dist, out):
    self.src = src
    self.dest = dest
    self.dist = dist
    self.out = out
  def getDist(self):
    return self.dist
  def getOut(self):
    return self.out
  def __str__(self):
    return str(self.src) + '->' + str(self.dest) + ' dist: ' + str(self.dist) + ' out: ' + str(self.out)



class Digraph(object):
   """
   A directed graph
   """
   def __init__(self):
       self.nodes = set([])
       self.edges = {}
   def addNode(self, node):
       if node in self.nodes:
           raise ValueError('Duplicate node')
       else:
           self.nodes.add(node)
           self.edges[node] = {}
   def addEdge(self, edge):
       src = edge.getSource()
       dest = edge.getDestination()
       dist = edge.getDist()
       out = edge.getOut()
       if not (src in self.nodes and dest in self.nodes):
           raise ValueError('Node not in graph')
       self.edges[src][dest] = (dist, out)
   def childrenOf(self, node):
       return self.edges[node]
   def hasNode(self, node):
       return node in self.nodes
   def __str__(self):
       res = ''
       for k in self.edges:
           for d in self.edges[k]:
               res = res + str(k) + '->' + str(d) + '\n'
       return res[:-1]
   def getLength(self, path):
      total = 0
      for i in range(len(path)-1):
        total += int(self.childrenOf(path[i])[path[i+1]][0])
      return total