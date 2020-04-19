import networkx as nx
import demon as d
import community as cm
import numpy as np


def set_community_attribute(G, communities, community_name):
    nx.set_node_attributes(G, 0, community_name)

    communityId = 1
    for community in communities:
        for id in community:
            node = G.nodes[id]
            node[community_name] = communityId
        communityId += 1


def add_kclique_community_attribute(G, k):
    communities = list(nx.algorithms.community.k_clique_communities(G, k))
    set_community_attribute(G, communities, 'kclique')


def add_demon_community_attribute(G):
    H = G.copy()
    dm = d.Demon(graph=H, epsilon=0.5, min_community_size=6)
    communities = dm.execute()
    set_community_attribute(G, communities, 'demon')


def add_louvain_community_attribute(G):
    communities = cm.best_partition(G, weight='gamecount')
    nx.set_node_attributes(G, communities, 'louvain')


def add_infomap_community_attribute(G):
    infomap = np.genfromtxt("infomap.txt", skip_header=True)
    nodes = infomap[:, 0]
    communities = infomap[:, 1]

    for i in range(len(nodes)):
        id = str(int(nodes[i]))
        node = G.nodes[id]
        node['infomap'] = communities[i]


def add_community_attributes(G):
    add_kclique_community_attribute(G, 6)
    add_demon_community_attribute(G)
    add_louvain_community_attribute(G)
    add_infomap_community_attribute(G)
    return G


network = nx.read_gexf('../graphs/chessnetwork_joined_filtered.gexf')
G = add_community_attributes(network)
nx.write_gexf(G, 'asd.gexf')
