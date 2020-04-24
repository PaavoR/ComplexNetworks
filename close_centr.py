# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:04:36 2020

@author: paavo.ronni
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import networkx as nx 

def plot_closeness_centrality(G, style):
    C_real = nx.closeness_centrality(G)
    G_deg = G.degree()
    
    deg_seq = {}
    
    for i in G_deg:
        deg_seq.setdefault(i[1],[]).append(i[0])
        
    centr_averages = {}    
        
    for key, value in deg_seq.items():
        betw_sum = 0
        for v in value:
            betw_sum += C_real[v]
        betw_sum = betw_sum / len(value)
        centr_averages[key] = betw_sum
    
    lists = sorted(centr_averages.items()) # sorted by key, return a list of tuples
    
    x, y = zip(*lists) # unpack a list of pairs into two tuples
        
    plt.plot(x,y,style)



G_real = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\chessnetwork_joined_filtered.gexf')
G_real = max(nx.connected_component_subgraphs(G_real), key=len)
plot_closeness_centrality(G_real,'o')

G_BA = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\\barabasi_albert_graph.gexf')
plot_closeness_centrality(G_BA,'og')

G_ER = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\erdos_renyi_graph.gexf')
plot_closeness_centrality(G_ER,'or')

plt.title("Closeness centrality")
plt.ylabel("Closeness centrality")
plt.xlabel("Degree k")
plt.legend(['Real','BA', 'ER'])

plt.show()