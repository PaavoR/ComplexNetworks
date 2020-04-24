# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:47:10 2020

@author: paavo.ronni
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import collections
from tqdm import tqdm

import networkx as nx 

G = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\chessnetwork_joined_filtered.gexf')
G = max(nx.connected_component_subgraphs(G), key=len)

N = len(G.nodes())

BA_G = nx.barabasi_albert_graph(N,8)

print('Number of edges: {}'.format(G.number_of_edges()))
print('Average degree: {}'.format(2.*G.number_of_edges()/
                                  G.number_of_nodes()))
degree_sequence = [degree for node, degree in G.degree()]
print('Max degree: {}'.format(max(degree_sequence)))
print('Network density: {}'.format(G.number_of_edges()/(N*(N-1)/2.)))
print('Average clustering coef.: {}'.format(nx.average_clustering(G)))

nx.write_gexf(BA_G,'barabasi_albert_graph.gexf')