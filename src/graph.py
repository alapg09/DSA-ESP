# graph.py
# Phase 2: Graph Generation (Barabási–Albert Model)

import networkx as nx

def generate_scale_free_graph(num_nodes=3000, m=4):
    """
    Generates a Barabási–Albert scale-free graph.
    
    :param num_nodes: total number of nodes
    :param m: number of edges to attach from a new node to existing nodes
    :return: generated graph G
    """
    print(f"Generating Barabási–Albert Graph with {num_nodes} nodes and m={m}...")
    
    G = nx.barabasi_albert_graph(num_nodes, m)

    print("Graph generated successfully!")
    print(f"Total Nodes: {G.number_of_nodes()}")
    print(f"Total Edges: {G.number_of_edges()}")

    return G
