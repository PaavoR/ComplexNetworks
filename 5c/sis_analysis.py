import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
import matplotlib.pyplot as plt
import numpy as np
import random

# Number of times the simulation is repeated
SIMULCOUNT = 1000
# Number of time steps in each simulation
ITERCOUNT = 50


def plot_spreading_figures(Si, Ii):
    plt.figure(1)
    for i in range(10):
        plt.plot(Ii[i], label=r'$Infected$')
    plt.xlabel(r'$t$', fontsize=16)
    plt.ylabel(r'$I(t)$', fontsize=16)
    plt.title(r'First 10 SIS-model simulations')

    Iavg = np.mean(Ii, axis=0)
    Savg = np.mean(Si, axis=0)
    plt.figure(2)
    plt.plot(Iavg, 'r', label=r'$Infected$')
    plt.plot(Savg, 'b', label=r'$Susceptible$')
    plt.xlabel(r'$t$', fontsize=16)
    plt.ylabel(r'$I(t), S(t)$', fontsize=16)
    plt.title(r'{0} SIS-model simulations: average susceptible and infected percentages'.format(SIMULCOUNT))
    plt.legend()

    Iend = np.array(Ii)
    Iend = Iend[:, -1]
    plt.figure(3)
    plt.hist(Iend)
    plt.ylabel('Frequency', fontsize=16)
    plt.xlabel('Infection percentage at end', fontsize=16)
    plt.title(r'{0} SIS-model simulations: percentage of infected nodes at end'.format(SIMULCOUNT))
    plt.show()


def simulate_sis_on_network(G):
    # Model Configuration
    cfg = mc.Configuration()
    cfg.add_model_parameter('beta', 0.05)
    cfg.add_model_parameter('lambda', 0.05)
    cfg.add_model_initial_configuration("Infected", random.sample(G.nodes, k=5))

    # Model selection
    model = ep.SISModel(G)

    # Initialize the simulation
    model.set_initial_status(cfg)

    Si, Ii = [], []
    for s in range(SIMULCOUNT):
        # Reset the model
        model.reset()

        # Simulation execution
        iterations = model.iteration_bunch(ITERCOUNT)

        # Collect results for figures
        S, I = [], []
        for i in range(ITERCOUNT):
            iteration = iterations[i]['node_count']
            S.append(iteration[0] / G.number_of_nodes())
            I.append(iteration[1] / G.number_of_nodes())
        Si.append(S)
        Ii.append(I)

    plot_spreading_figures(Si, Ii)


# SIS simulation on the chess network
G = nx.read_gexf('../graphs/chessnetwork_giant.gexf')
simulate_sis_on_network(G)

# SIS simulation on the Barabasi Albert network
G = nx.read_gexf('../graphs/barabasi_albert_graph.gexf')
simulate_sis_on_network(G)

# SIS simulation on the Erdos Renyi network
G = nx.read_gexf('../graphs/erdos_renyi_graph.gexf')
simulate_sis_on_network(G)
