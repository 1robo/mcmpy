### Day3 简单图论模型 范例程序2 ###

# 更多的networkx用法
# 参考官方文档 https://networkx.github.io/documentation/latest/tutorial.html

import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
nlist = ['A','B','C','D']
G.add_nodes_from(nlist)
G.add_edge('A', 'B',weight=1)
G.add_edge('B', 'C',weight=1)
G.add_edge('C', 'D',weight=1)
G.add_edge('A', 'D',weight=1)
G.add_edge(nlist[0],nlist[2])
nx.draw_networkx(G)
print(nx.shortest_path(G, 'A', 'C', weight='weight'))   
plt.show()
