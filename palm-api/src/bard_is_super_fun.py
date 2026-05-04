import graphviz as gv
import networkx as nx

thingy = gv.Source.from_file('graph.dot')
#print(str(thingy))
gv = gv.Graph('graph.dot')
G = nx.DiGraph(gv)

nx.draw(G)
