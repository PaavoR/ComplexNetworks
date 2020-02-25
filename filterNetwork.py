import networkx as nx 


def remove_links_with_gamecount_less_than(network, gamecount):
    network.remove_edges_from([(u,v) for u,v,e in network.edges(data=True) if e['gamecount'] < gamecount])
    print(network.number_of_edges())


network = nx.read_gexf('chessnetwork.gexf')
remove_links_with_gamecount_less_than(network,2)
nx.write_gexf(network, "chessnetwork_filtered.gexf")