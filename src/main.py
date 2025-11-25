# main.py
# Entry point for running project phases

from graph import generate_scale_free_graph
from visualize import visualize_graph

def main():
    # Phase 2: Generate Graph
    G = generate_scale_free_graph(num_nodes=3000, m=4)

    # Phase 3: Visualize Graph
    visualize_graph(G, filename="network.png")

    print("\nPhase 3 complete. Graph visualization created.")

if __name__ == "__main__":
    main()
