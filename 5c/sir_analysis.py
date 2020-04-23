import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
import matplotlib.pyplot as plt
import numpy as np
import random

# Number of times the simulation is repeated
SIMULCOUNT = 1000
# Number of time steps in each simulation
ITERCOUNT = 100


def plot_spreading_figures(Si, Ii, Ri):
    plt.figure(1)
    for i in range(10):
        plt.plot(Ii[i], label=r'$Infected$')
    plt.xlabel(r'$t$', fontsize=16)
    plt.ylabel(r'$I(t)$', fontsize=16)
    plt.title(r'First 10 SIR-model simulations')

    Iavg = np.mean(Ii, axis=0)
    Savg = np.mean(Si, axis=0)
    Ravg = np.mean(Ri, axis=0)
    plt.figure(2)
    plt.plot(Iavg, 'r', label=r'$Infected$')
    plt.plot(Savg, 'b', label=r'$Susceptible$')
    plt.plot(Ravg, 'g', label=r'Recovered')
    plt.xlabel(r'$t$', fontsize=16)
    plt.ylabel(r'$I(t), S(t), R(t)$', fontsize=16)
    plt.title(r'{0} SIR-model simulations: average susceptible, infected and recovered percentages'.format(SIMULCOUNT))
    plt.legend()

    Rend = np.array(Ri)
    Rend = Rend[:, -1]
    plt.figure(3)
    plt.hist(Rend)
    plt.xlabel(r'$t$', fontsize=16)
    plt.ylabel(r'$Frequency$', fontsize=16)
    plt.title(r'{0} SIR-model simulations: percentage of recovered nodes at end'.format(SIMULCOUNT))
    plt.legend()
    plt.show()


def simulate_sir_on_network(G):
    # Model Configuration
    cfg = mc.Configuration()
    cfg.add_model_parameter('beta', 0.05)
    cfg.add_model_parameter('gamma', 0.05)
    cfg.add_model_initial_configuration("Infected", random.sample(G.nodes, k=5))

    # Model selection
    model = ep.SIRModel(G)

    # Initialize the simulation
    model.set_initial_status(cfg)

    Si, Ii, Ri = [], [], []
    for s in range(SIMULCOUNT):
        # Reset the model
        model.reset()

        # Simulation execution
        iterations = model.iteration_bunch(ITERCOUNT)

        # Collect results for figures
        S, I, R = [], [], []
        for i in range(ITERCOUNT):
            iteration = iterations[i]['node_count']
            S.append(iteration[0] / G.number_of_nodes())
            I.append(iteration[1] / G.number_of_nodes())
            R.append(iteration[2] / G.number_of_nodes())
        Si.append(S)
        Ii.append(I)
        Ri.append(R)

    plot_spreading_figures(Si, Ii, Ri)


# SIS simulation on the chess network
G = nx.read_gexf('../graphs/chessnetwork_giant.gexf')
simulate_sir_on_network(G)

# SIS simulation on the Barabasi Albert network
G = nx.read_gexf('../graphs/barabasi_albert_graph.gexf')
simulate_sir_on_network(G)

# SIS simulation on the Erdos Renyi network
G = nx.read_gexf('../graphs/erdos_renyi_graph.gexf')
simulate_sir_on_network(G)


