import networkx as nx
import matplotlib.pyplot as plt

def generalized_petersen_graph(n, k):
    return nx.generators.classic.generalized_petersen_graph(n, k)

G = generalized_petersen_graph(7, 2)
nx.draw(G, with_labels=True, node_color="orange", node_size=500)
plt.show()
