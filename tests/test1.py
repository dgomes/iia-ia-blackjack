#encoding: utf8
import sys
sys.path.insert(0,"..")
from game import Game
from player import Player
from testplayer import TestPlayer
from card import Card
from test_shoe import TestShoe

if __name__ == '__main__':

    players = [TestPlayer("test",100)]

    print players
    g = Game(players, debug=True, shoe=TestShoe([Card(0,1), Card(0,2), Card(1,1), Card(1,12)] )) 
    g.run()

    print "OVERALL: ", players
    if str(players) == "[test (99€)]":
        sys.exit(0) 
    sys.exit(1) 
