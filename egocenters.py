import networkx as nx


def find_impostor(edgelist, pseudocenters):
    G = nx.Graph(edgelist)
    sub_graphs = [nx.ego_graph(G, center) for center in pseudocenters]

    for i, graph in enumerate(sub_graphs):
        graphs_to_combine = sub_graphs[:i] + sub_graphs[i + 1:]
        union_graph = nx.Graph()
        for g in graphs_to_combine:
            union_graph = nx.compose(union_graph, g)
        if nx.faster_could_be_isomorphic(union_graph, G):
            return pseudocenters[i]
