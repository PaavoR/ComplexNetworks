# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:49:28 2020

@author: paavo.ronni
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import collections
from scipy.optimize import curve_fit

import networkx as nx 

G = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\chessnetwork_joined_filtered.gexf')
G = max(nx.connected_component_subgraphs(G), key=len)

N = len(G.nodes())
k = 2.*G.number_of_edges()/G.number_of_nodes()
p = k/(N-1)

ER_G = nx.erdos_renyi_graph(N,p)
print(len(ER_G.nodes()))
G_ER_Giant = max(nx.connected_component_subgraphs(ER_G), key=len)
print(len(G_ER_Giant .nodes()))
nx.write_gexf(ER_G,'erdos_renyi_graph.gexf')