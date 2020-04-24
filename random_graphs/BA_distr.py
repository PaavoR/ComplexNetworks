# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:43:20 2020

@author: paavo.ronni
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import collections
from scipy.optimize import curve_fit

import networkx as nx 

G = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\\barabasi_albert_graph.gexf')
G = max(nx.connected_component_subgraphs(G), key=len)

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
plt.ylim(top=1)
plt.ylim(bottom=10e-5)
plt.xlim(left=5)
plt.xlim(right=250)

def func_powerlaw(x, m, c):
    return x**m * c

target_func = func_powerlaw
popt, pcov = curve_fit(target_func, deg, prob_k, maxfev=3000)


plt.plot(deg,target_func(deg,*popt), '--')
#plt.gca().set_aspect('equal', adjustable='box')
plt.loglog()
