# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:00:53 2020

@author: paavo.ronni
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import networkx as nx 



def plot_clustering(G_real, style):
    C_real = nx.clustering(G_real)
    G_deg = G_real.degree()
    
    deg_seq = {}
    
    for i in G_deg:
        deg_seq.setdefault(i[1],[]).append(i[0])
        
    clustering_averages = {}    
        
    for key, value in deg_seq.items():
        clust_sum = 0
        for v in value:
            clust_sum += C_real[v]
        clust_sum = clust_sum / len(value)
        clustering_averages[key] = clust_sum
    
    lists = sorted(clustering_averages.items()) # sorted by key, return a list of tuples
    
    x, y = zip(*lists) # unpack a list of pairs into two tuples
        
    plt.plot(x,y,style)

G = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\chessnetwork_joined_filtered.gexf')
G_real = max(nx.connected_component_subgraphs(G), key=len)
plot_clustering(G_real,'o')

G_BA = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\\barabasi_albert_graph.gexf')
plot_clustering(G_BA,'og')

G_ER = nx.read_gexf('C:\OmatProjektit\ComplexNetworks\graphs\erdos_renyi_graph.gexf')
plot_clustering(G_ER,'or')

print('Average clustering coef. real: {}'.format(nx.average_clustering(G_real)))
print('Average clustering coef.BA: {}'.format(nx.average_clustering(G_BA)))
print('Average clustering coef.ER: {}'.format(nx.average_clustering(G_ER)))

plt.title("Clustering coefficient")
plt.ylabel("Clustering coefficient")
plt.xlabel("Degree k")
plt.legend(['Real','BA', 'ER'])



plt.show()
    

