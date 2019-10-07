### Day3 简单图论模型 范例程序1 ###
# 更多的networkx用法
# 参考官方文档 https://networkx.github.io/documentation/latest/tutorial.html
import warnings
warnings.filterwarnings("ignore")  #忽略警告
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
nlist = ['A','B','C','D']
G.add_nodes_from(nlist)
elist = [('A','B'),('B','C'),('C','D'),('A','D')]
G.add_edges_from(elist)
nx.draw_networkx(G)
print(nx.shortest_path(G, 'A', 'C'))
print(nx.shortest_path_length(G, 'A', 'C'))
plt.show()

