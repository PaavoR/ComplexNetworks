import networkx as nx 

def print_graph_info(G):
    N = G.number_of_nodes()
    largest_cc = max(nx.connected_components(G), key=len)
    G_giant = nx.subgraph(G, largest_cc)    
    
    print('Number of nodes: {}'.format(G.number_of_nodes()))
    print('Number of edges: {}'.format(G.number_of_edges()))
    print('Average degree: {}'.format(2.*G.number_of_edges()/G.number_of_nodes()))
    degree_sequence = [degree for node, degree in G.degree()]
    print('Max degree: {}'.format(max(degree_sequence)))
    print('Network density: {}'.format(G.number_of_edges()/(N*(N-1)/2.)))
    print('Average clustering coef.: {}'.format(nx.average_clustering(G)))
    print('Giant component: {}'.format(G_giant.number_of_nodes()))
    print('GC Average shortest path length: {}'.format(nx.average_shortest_path_length(G_giant)))

network = nx.read_gexf('chessnetwork.gexf')
network_filtered = nx.read_gexf('chessnetwork_filtered2.gexf')
G = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\chessnetwork_joined_filtered.gexf')
G_giant = max(nx.connected_component_subgraphs(G), key=len)
#print_graph_info(network)
#print_graph_info(network_filtered)
print_graph_info(G_giant)