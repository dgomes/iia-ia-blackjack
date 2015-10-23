from game import Game
from player import Player
from randomplayer import RandomPlayer

if __name__ == '__main__':

    players = [RandomPlayer("Human",100)]

    for i in range(100):
        print players
        g = Game(players) 
        #g = Game(players, debug=True)
        g.run()

    print "OVERALL: ", players
