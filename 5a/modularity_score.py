import networkx as nx


def group_nodes_in_same_community(G, communityname, zeroIdToUnique):
    communityid_nodeset_dict = dict()
    uniqueId = 10000

    for nodeid in G.nodes:
        node = G.nodes[nodeid]
        communityid = node[communityname]

        if communityid == 0 and zeroIdToUnique is True:
            communityid_nodeset_dict[uniqueId] = [nodeid]
            uniqueId = uniqueId + 1
            continue

        if communityid in communityid_nodeset_dict:
            communityid_nodeset_dict[communityid].append(nodeid)
        else:
            communityid_nodeset_dict[communityid] = [nodeid]

    return communityid_nodeset_dict


network = nx.read_gexf('./asd.gexf')
giant = max(nx.connected_components(network), key=len)
giant = network.subgraph(giant)

community_dict = group_nodes_in_same_community(giant, "kclique", True)
communities_kclique = list(community_dict.values())

community_dict = group_nodes_in_same_community(giant, "demon", True)
communities_demon = list(community_dict.values())

community_dict = group_nodes_in_same_community(giant, "louvain", True)
communities_louvain = list(community_dict.values())

community_dict = group_nodes_in_same_community(giant, "infomap", True)
communities_infomap = list(community_dict.values())

print("Modularity")
print("K-Clique: {0}".format(nx.algorithms.community.modularity(giant, communities_kclique)))
print("Demon: {0}".format(nx.algorithms.community.modularity(giant, communities_demon)))
print("Louvain: {0}".format(nx.algorithms.community.modularity(giant, communities_louvain)))
print("Infomap: {0}".format(nx.algorithms.community.modularity(giant, communities_infomap)))
