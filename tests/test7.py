#encoding: utf8
import sys
sys.path.insert(0,"..")
from game import Game
from player import Player
from card import Card
from test_shoe import TestShoe

# Double down max bet
class TestPlayer(Player):
    def __init__(self, name="TestPlayer", money=0, default_bet=1):
        super(TestPlayer, self).__init__(name, money)
        self.default_bet = default_bet

    def play(self, dealer, players):
        print("SURRENDER")
        return "u"

    def bet(self, dealer, players):
        return 4 

if __name__ == '__main__':

    players = [TestPlayer("test",100)]

    print(players)
    g = Game(players, debug=True, shoe=TestShoe([Card(3,12), Card(3,6), Card(1,2), Card(1,8), Card(2,4), Card(3,3)] ))
    g.run()

    print("OVERALL: ", players)
    if str(players) == "[test (100€)]":
        sys.exit(0)
    sys.exit(1)
