# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import networkx as nx

def joinFideData(G):
    notFound = 0
    df = pd.read_fwf('data/players_list_foa.txt')
    df =df[['ID Number','Fed', 'Sex', 'B-day']]
    df.set_index(['ID Number'], inplace=True)
    for node in G.nodes():
        id = G.node[node]['label']
        id_int = int(id)
        try:

            row = df.loc[id_int]
            fed = row['Fed']
            sex = row['Sex']
            b_day = row['B-day']
            G.node[node]["Fed"] = fed
            G.node[node]["Sex"] = sex
            G.node[node]["B-day"] = b_day
        except:
            print("Not found " + id)
            notFound+=1
    print('Not found ')
    print(notFound)

            
    
network = nx.read_gexf('chessnetwork.gexf')
joinFideData(network)
nx.write_gexf(network,'chessnetwork_joined.gexf')
