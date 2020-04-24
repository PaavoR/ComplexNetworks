# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:08:23 2020

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

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

plt.bar(deg, cnt, width=0.80, color='b')
plt.title('Degree Histogram')
plt.ylabel("Count")
plt.xlabel("Degree")
plt.xticks([d + 0.4 for d in deg[0::10]], labels=deg[0::10])

plt.plot()