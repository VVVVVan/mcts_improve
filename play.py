import Arena
from MCTS import MCTS
from othello.OthelloGame import OthelloGame
from othello.OthelloPlayers import RandomPlayer, GreedyOthelloPlayer
from othello.NNet import NNetWrapper as NNet
import numpy as np
from utils import *

"""
This script is used to get the number of win for trained nn and ramdon/greedy player.
Remember to store the ouput in a file, so that could be further used to plot.
"""
args = dotdict({ 
    'numIters': 20,
    'numGames': 100,
    'checkpoint': './temp/20_8checkpoints/',
})

if __name__ == "__main__":
    g = OthelloGame(8)

    # all players
    rp = RandomPlayer(g).play
    gp = GreedyOthelloPlayer(g).play

    print("Iteration 0")
    print('Random players')
    arena_r = Arena.Arena(rp, rp, g, display=OthelloGame.display)
    print(arena_r.playGames(args.numGames, verbose=True))

    print('Greedy players')
    arena_g = Arena.Arena(rp, gp, g, display=OthelloGame.display)
    print(arena_g.playGames(args.numGames, verbose=True))

    for i in range(1,args.numIters):
        print('Iteration', i)
        filename = 'checkpoint_{i}.pth.tar'.format(i=i)
        # player
        n1 = NNet(g)
        n1.load_checkpoint(args.checkpoint, filename)
        args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
        mcts1 = MCTS(g, n1, args1)
        n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

        # Random players
        print('Random players')
        arena_r = Arena.Arena(n1p, rp, g, display=OthelloGame.display)
        print(arena_r.playGames(args.numGames, verbose=True))

        # Greedy players
        print('Greedy players')
        arena_g = Arena.Arena(n1p, gp, g, display=OthelloGame.display)
        print(arena_g.playGames(args.numGames, verbose=True))
