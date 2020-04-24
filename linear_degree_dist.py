# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:39:37 2020

@author: paavo.ronni
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:02:56 2020

@author: paavo.ronni
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import collections
from scipy.optimize import curve_fit

import networkx as nx 

G = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\chessnetwork_joined_filtered.gexf')
#G = max(nx.connected_component_subgraphs(G), key=len)

N = len(G.nodes())

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

f_count = [float(i) for i in cnt]
prob_k = [x / N for x in f_count]


plt.scatter(deg, prob_k, marker='o')
plt.title("Degree distribution")
plt.ylabel("P(k)")
plt.xlabel("Degree")

plt.plot()