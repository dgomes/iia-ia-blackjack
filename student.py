#encoding: utf8
import card
import random
from player import Player

class StudentPlayer(Player):
    def __init__(self, name="Meu nome", money=0):
        super(StudentPlayer, self).__init__(name, money)

    def play(self, dealer, players):
        return "s"

    def bet(self, dealer, players):
        return 1 
