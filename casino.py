from game import Game
from player import Player
from randomplayer import RandomPlayer

if __name__ == '__main__':

    players = [Player("Human",100)]

    for i in range(100):
        print players
        g = Game(players, min_bet=1, max_bet=5) 
        #g = Game(players, debug=True)
        g.run()

    print "OVERALL: ", players
