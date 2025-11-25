import networkx as nx
import matplotlib.pyplot as plt
import os

def visualize_graph(G, filename="network.png"):
    """
    Draws a force-directed (spring layout) visualization of the network.
    Saves the output as an image inside /results/.
    """
    print("Generating force-directed visualization...")

    # Create results directory
    os.makedirs("../results", exist_ok=True)

    # Spring layout: force-directed graph drawing
    pos = nx.spring_layout(G, seed=42, k=0.1, iterations=50)

    plt.figure(figsize=(12, 12))

    # Draw nodes (small size for clarity)
    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=10,
        node_color="lightblue",
        alpha=0.8
    )

    # Draw edges (very light for readability)
    nx.draw_networkx_edges(
        G,
        pos,
        width=0.2,
        alpha=0.3,
        edge_color="gray"
    )

    plt.title("Force-Directed Visualization of Barabási–Albert Network", fontsize=14)
    plt.axis("off")

    # Save output
    save_path = f"../results/{filename}"
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Visualization saved to {save_path}")
