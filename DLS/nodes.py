import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
H = nx.path_graph(25)

G.add_edges_from([[0,1], [0,2], [0,3], [0,4], [0,5], [0,6]])
G.add_edges_from([[1,7], [1,8], [1,9], [1, 10]])
G.add_edges_from([[2, 11], [2,12], [2,13]])
G.add_edges_from([[3, 14], [3,15], [3,16]])
G.add_edges_from([[4, 17], [4,18], [4,19]])
G.add_edges_from([[5, 20], [5,21], [5,22]])
G.add_edges_from([[6, 23], [6,24], [2,25]])

# G.add_edges_from([(1, 2), (1, 3)])
# G.add_edges_from(H.edges)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=1000)
plt.show()
