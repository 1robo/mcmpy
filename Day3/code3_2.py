### Day3 简单图论模型 范例程序2 ###

# 更多的networkx用法
# 参考官方文档 https://networkx.github.io/documentation/latest/tutorial.html
import warnings
warnings.filterwarnings("ignore")  #忽略警告
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_node(1,pos=(1,1))
G.add_node(2,pos=(2,2))
G.add_node(3,pos=(3,2))
G.add_node(4,pos=(3,3))
G.add_node(5,pos=(4,3))
G.add_edge(1,2,weight=10.5)
G.add_edge(1,3,weight=9.8)
G.add_edge(2,4,weight=2)
G.add_edge(4,5,weight=3.2)
G.add_edge(3,5,weight=6)
pos=nx.get_node_attributes(G,'pos')
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
print("1 到 5 的最短路径是")
print(nx.shortest_path(G,1,5,weight='weight')) 
print(nx.shortest_path_length(G,1,5,weight='weight')) 
print("最小生成树是")
print(nx.minimum_spanning_tree(G).edges()) # algorithm with prim 

plt.show()
