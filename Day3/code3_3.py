### Day3 简单图论模型 范例程序3 ###
###   通过图论解决过河问题      ###

# 更多的networkx用法
# 参考官方文档 https://networkx.github.io/documentation/latest/tutorial.html
import warnings
warnings.filterwarnings("ignore")  #忽略警告
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nlist = ['ABCD|','BD|AC','ABC|D','ABD|C','ACD|B','B|ACD','C|ABD','D|ABC','AC|BD','|ABCD']
G.add_nodes_from(nlist)
G.add_edge(nlist[0], nlist[1])
G.add_edge(nlist[1], nlist[3])
G.add_edge(nlist[2], nlist[5])
G.add_edge(nlist[2], nlist[6])
G.add_edge(nlist[3], nlist[5])
G.add_edge(nlist[3], nlist[7])
G.add_edge(nlist[4], nlist[6])
G.add_edge(nlist[4], nlist[7])
G.add_edge(nlist[6], nlist[8])
G.add_edge(nlist[8], nlist[9])

nx.draw_networkx(G)
print(nx.shortest_path(G, nlist[0], nlist[9], weight='weight'))
plt.show()
