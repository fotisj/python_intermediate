import networkx as nx
#import matplotlib.pyplot as plt
import pylab

g = nx.Graph()

"""
g.add_nodes_from(["A","B","C"])
g.add_edges_from([("A","B"), ("B","C"), ("A","C")])
#g.add_edges_from([("Schiller","Humboldt",{"weight": 3}), ("Goethe","Schiller",{"weight": 8}), ("Goethe","Humboldt", {"weight": 5})])
"""
g.add_nodes_from(["Goethe", "Schiller", "Zelter"])
g.add_edge("Goethe","Zelter",weight=3)
g.add_edge("Goethe","Schiller",weight=6),
g.add_edge("Goethe","Humboldt", weight=5)

for u,v,d in g.edges(data=True): 
    print("u " + u)
    print("v " + v)
    print("d " + str(d))


#pos (regelt das layout) muss nach der Beschreibung des Graphen stehen!
pos=nx.spring_layout(g)

pylab.figure(1)

nx.draw_networkx_nodes(g, pos)
nx.draw_networkx_edge_labels(g,pos)
nx.draw_networkx_edges(g,pos)

#edge_labels=dict([((u,v,),d['weight']) for u,v,d in g.edges(data=True)])
#nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels)


"""
nx.draw_networkx_edges(g, pos, edgelist=[["Schiller","Humboldt"]], width=3)
nx.draw_networkx_edges(g, pos, edgelist=[["Goethe","Schiller"]], width=6)
nx.draw_networkx_edges(g, pos, edgelist=[["Goethe","Humboldt"]], width=5)
"""

pylab.show()
