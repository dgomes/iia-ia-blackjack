#encoding: utf8
__author__ = 'Diogo Gomes'
__email__ = 'dgomes@ua.pt'
__license__ = "GPL"
__version__ = "0.1"
import card
import random
from player import Player

class TestPlayer(Player):
    def __init__(self, name="TestPlayer", money=0, default_bet=1):
        super(TestPlayer, self).__init__(name, money)
        self.default_bet = default_bet

    def play(self, dealer, players):
        return "h"

    def bet(self, dealer, players):
        return self.default_bet 
