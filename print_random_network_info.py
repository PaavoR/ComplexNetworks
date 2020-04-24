# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:54:43 2020

@author: paavo.ronni
"""
import networkx as nx

G_real = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\chessnetwork_joined_filtered.gexf')
G_real = max(nx.connected_component_subgraphs(G_real), key=len)


G_BA = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\\barabasi_albert_graph.gexf')


G_ER = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\erdos_renyi_graph.gexf')


networks = [G_real,G_BA,G_ER]
for G in networks:
    largest_cc = max(nx.connected_components(G), key=len)
    G_giant = nx.subgraph(G, largest_cc) 
    print('Number of nodes: {}'.format(G.number_of_nodes()))
    print('Number of edges: {}'.format(G.number_of_edges()))
    print('Average degree: {}'.format(2.*G.number_of_edges()/G.number_of_nodes()))
    print('Giant component: {}'.format(G_giant.number_of_nodes()))