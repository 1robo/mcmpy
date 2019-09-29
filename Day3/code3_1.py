import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
nlist = ['A','B','C','D']
G.add_nodes_from(nlist)
elist = [('A','B'),('B','C'),('C','D'),('A','D'),('A','C')]
G.add_edges_from(elist)
nx.draw_networkx(G)
print(G.number_of_edges())
print(nx.shortest_path(G, 'A', 'C', weight='weight'))   
plt.show()
