from game import Game
from player import Player

if __name__ == '__main__':

    players = [Player("Human",100)]

    for i in range(3):
        print players
        g = Game(players)
        g.run()

    print "OVERALL: ", players
