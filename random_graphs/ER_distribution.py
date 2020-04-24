# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:13:19 2020

@author: paavo.ronni
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import collections
from scipy.stats import binom

import networkx as nx 

G = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\erdos_renyi_graph.gexf')
G = max(nx.connected_component_subgraphs(G), key=len)

N = len(G.nodes())

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

f_count = [float(i) for i in cnt]
prob_k = [x / N for x in f_count]

k = 2.*G.number_of_edges()/G.number_of_nodes()
p = k/(N-1)
k = range(N-1)
p_k = binom.pmf(k=k, n=N, p=p)
plt.plot(k, p_k,'g-')



plt.scatter(deg, prob_k, marker='o')
plt.title("Degree distribution and binomial prediction")
plt.ylabel("P(k)")
plt.xlabel("Degree")
plt.ylim(top=0.2)
plt.ylim(bottom=10e-5)
plt.xlim(left=1)
plt.xlim(right=30)

plt.plot()