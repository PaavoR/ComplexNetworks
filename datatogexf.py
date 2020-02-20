import networkx as nx
import chess.pgn

# read the game database.
pgn = open("./data/caissabasepgn.pgn", encoding='utf-8')

# create empty graph.
G = nx.Graph()

# chess players are rated using ELO-rating.
# https://en.wikipedia.org/wiki/Elo_rating_system
def calculate_elo_change(ratingWhite, ratingBlack, result):
    # map actual game result from -1, 0, 1 to 0, 1/2, 1
    if result == 0:
        result = 0.5
    elif result == -1:
        result = 0

    K = 10 # K-factor used by FIDE (https://ratings.fide.com/calculator_rtd.phtml)
    expectedResult = 1 / (1 + 10 ** ((ratingBlack - ratingWhite) / 400))  # between 0...1
    return round(K * (result - expectedResult), 1)  # ratings are given with 1 decimal accuracy.


def get_result_and_elo_change(game):
    eloWhite = int(game.headers['WhiteElo'])
    eloBlack = int(game.headers['BlackElo'])
    result = game.headers["Result"]

    if result == "1-0":
        result = 1
    elif result == "0-1":
        result = -1
    else:
        result = 0

    eloChange = calculate_elo_change(eloWhite, eloBlack, result)
    return result, eloChange


# network nodes are the chess players.
def add_or_update_network_node(network, id, name, elo, result, eloChange):
    win = 0
    draw = 0
    loss = 0
    if result == 1:
        win = 1
    elif result == 0:
        draw = 1
    else:
        loss = 1

    # if node already exists, update node attributes.
    if network.has_node(id):
        node = network.nodes[id]
        node['gamecount'] += 1
        node['elosum'] += eloChange

        # new max rating?
        if elo > node['maxrating']:
            node['maxrating'] = elo

        # new min rating?
        if elo < node['minrating']:
            node['minrating'] = elo

        # save game result.
        node['wins'] += win
        node['draws'] += draw
        node['losses'] += loss

    # otherwise, create a new node.
    else:
        network.add_node(id,
                         name=name,
                         gamecount=1,
                         maxrating=elo,
                         minrating=elo,
                         elosum=eloChange,
                         wins=win,
                         draws=draw,
                         losses=loss)


# Network edges are the games between the players.
def add_or_update_network_edge(network, idWhite, idBlack, result, eloChange):
    # Normally results are reported relative to colors: white wins -> (1-0), black wins -> (0-1), draw -> (1/2-1/2).
    # Problem: players can change color between games.
    # To track results we normalize the results so that:
    # + is good for player with smaller id and - is good for player with larger id.
    if idWhite > idBlack:
        result = -1 * result
        eloChange = -1 * result

    # If edge already exists, update edge attributes.
    if network.has_edge(idWhite, idBlack):
        edge = network.edges[idWhite, idBlack]
        edge["gamecount"] += 1
        edge["score"] += result
        edge["elosum"] += eloChange

    # Otherwise, create a new edge.
    else:
        network.add_edge(idWhite, idBlack,
                         gamecount=1,
                         score=result,
                         elosum=eloChange)


def add_game_to_network(network, game):
    idWhite = int(game.headers['WhiteFideId'])
    idBlack = int(game.headers['BlackFideId'])
    result, eloChange = get_result_and_elo_change(game)

    # 1) add/update the player nodes.
    add_or_update_network_node(network, idWhite, game.headers['White'], int(game.headers['WhiteElo']), result, eloChange)
    add_or_update_network_node(network, idBlack, game.headers['Black'], int(game.headers['BlackElo']), -result, -eloChange)

    # 2) add/update the edge between the player nodes.
    add_or_update_network_edge(network, idWhite, idBlack, result, eloChange)


# read database
pgn = open("./data/caissabasepgn.pgn", encoding='utf-8')

gameCount = 0
discardedCount = 0
while True:
    # read next game in the database.
    game = chess.pgn.read_game(pgn)

    # stop if all games parsed.
    if game is None:
        break

    # discard games: missing information or low rating.
    if 'WhiteElo' not in game.headers or game.headers['WhiteElo'] == '?' or int(game.headers['WhiteElo']) < 2400 \
            or 'BlackElo' not in game.headers or game.headers['BlackElo'] == '?' or int(game.headers['BlackElo']) < 2400 \
            or 'Event' not in game.headers or game.headers['Event'] == '?' \
            or 'WhiteFideId' not in game.headers or game.headers['WhiteFideId'] == '?' \
            or 'BlackFideId' not in game.headers or game.headers['BlackFideId'] == '?':
        discardedCount += 1
        continue

    # if the game passed all checks, add the game to our network.
    add_game_to_network(G, game)

    # show progress.
    if gameCount % 100 == 0:
        print("Games in network: {0}, discarded: {1}, total: {2}".format(gameCount, discardedCount, gameCount + discardedCount))
    gameCount += 1

# save the network in .gexf format for Gephi.
nx.write_gexf(G, "chessnetwork.gexf")




