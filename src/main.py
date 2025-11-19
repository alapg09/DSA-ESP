# main.py
# Entry point for running the project

from graph import generate_scale_free_graph

def main():
    # Phase 2: Test Graph Generation
    G = generate_scale_free_graph(num_nodes=3000, m=4)

    # (Optional) Print some basic info
    print("\nSample of node degrees:")
    print(sorted([d for _, d in G.degree()], reverse=True)[:10])
    print("\nGraph generation phase complete.")

if __name__ == "__main__":
    main()
    