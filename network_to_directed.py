import networkx as nx 

def network_to_directed(network):
    G = nx.DiGraph()
    G.add_nodes_from(network.nodes())
    for u,v,e in network.edges(data=True):
        u = int(u)
        v = int(v)
        if e['score'] <= 0:
            G.add_edge(max(v,u), min(u,v),
                         gamecount=e['gamecount'],
                         score=e['score'])
        if e['score'] >= 0:
            G.add_edge(min(v,u), max(v,u),
                         gamecount=e['gamecount'],
                         score=e['score'])
    return G


network = nx.read_gexf('chessnetwork.gexf')
directed_network = network_to_directed(network)
nx.write_gexf(directed_network, "chessnetwork_directed.gexf")

network = nx.read_gexf('chessnetwork_filtered.gexf')
directed_network = network_to_directed(network)
nx.write_gexf(directed_network, "chessnetwork_filtered_directed.gexf")