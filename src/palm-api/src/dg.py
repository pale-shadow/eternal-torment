# import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

G.add_node("google_container_node_pool", shape="box")
G.add_node("google_container_cluster.primary", shape="box")
G.add_node("google_compute_subnetwork.gke-subnet", shape="box")
G.add_node("google_compute_router.router", shape="box")
G.add_node("google_compute_network.mgmt-vpc", shape="box")

G.add_edge("google_container_node_pool", "google_container_cluster.primary")
G.add_edge("google_container_node_pool", "google_container_cluster.primary")
G.add_edge("google_container_cluster.primary", "google_compute_subnetwork.gke-subnet")
G.add_edge("google_container_cluster.primary", "google_compute_router.router")
G.add_edge("google_container_cluster.primary", "google_compute_network.mgmt-vpc")
G.add_edge("google_compute_router.router", "google_compute_network.mgmt-vpc")
G.add_edge("google_compute_subnetwork.gke-subnet", "google_compute_network.mgmt-vpc")

print("Edges in G: ", G.edges(data=True))
