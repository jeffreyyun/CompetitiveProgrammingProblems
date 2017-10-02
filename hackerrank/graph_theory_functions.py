class Node:
	pass

class Edge:
	pass

def bfs(adj, v, count):
	q = queue.Queue()
	q.add(v)
	while not q.empty():
		v = q.pop()
		for neighbor in adj[v]:
			q.add(neighbor)
		doSomething()
	return

def dfs(adj, v, count):
	stk = [v]
	while len(stk) > 0:
		v = stk.pop()
		for neighbor in adj[v]:
			stk.append(neighbor)
		doSomething()
	return



def get_weight():


def dijkstra():



def bellman_ford():



def kruskal():	# or prim()
