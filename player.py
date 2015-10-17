#encoding: utf8
__author__ = 'Diogo Gomes'
__email__ = 'dgomes@ua.pt'
__license__ = "GPL"
__version__ = "0.1"
import card

class Player(object):
    def __init__(self, name="Player", money=0):
        self.hand = []
        self.name = name
        self.pocket = money

    def __str__(self):
        return "{} ({}€)".format(self.name, self.pocket)

    def __repr__(self):
        return self.__str__()

    def getHand(self):
        return self.hand

    def payback(self, prize):
        """ receives bet + premium
            or 0 if player lost
        """
        self.pocket += prize

    def play(self, dealer, players):
        """ Calculates decision to take
            Must be either "h" or "s"
        """
        print "DEALER: ", dealer
        return raw_input("(h)it or (s)tand  ")

    def bet(self, dealer, players):
        """ Calculates how much to bet

            dealer - state
            players - list of players state
            bet (int value)
        """
        print "DEALER: ", dealer
        try:
            bet = int(raw_input("bet: "))
        except Exception, e:
            bet = 1
        self.pocket-=bet
        return bet
