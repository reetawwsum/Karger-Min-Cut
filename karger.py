from random import choice
from collections import Counter
from copy import deepcopy

g = {}

def kargerMinCut(g):
	while len(g) > 2:
		#Selecting a random vertex
		u = choice(g.keys())
		gu = g[u]
		#Selecting most comman vertex among the previously chosen random vertex
		v = gu.most_common(1)[0][0]
		gv = g[v]
		#Deleting second vertex from the graph
		del g[v]
		#Deleting self loop
		del gv[u]
		del gu[v]
		#Merging second vertex into first vertex
		gu.update(gv)
		for w in gv:
			gw = g[w]
			gw[u] += gw[v]
			del gw[v]
	return g.itervalues().next().most_common(1)[0][1]

with open('kargerMinCut.txt', 'r') as graphInput:
	for line in graphInput:
		ints = [int(x) for x in line.split()]
		g[ints[0]] = Counter(ints[1:])

cuts = [kargerMinCut(deepcopy(g)) for x in range(5)]

print min(cuts), cuts