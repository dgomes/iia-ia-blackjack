#encoding: utf8
__author__ = 'Diogo Gomes'
__email__ = 'dgomes@ua.pt'
__license__ = "GPL"
__version__ = "0.1"
import card

class Player(object):
    def __init__(self, name="Player", money=0):
        self.name = name
        self.pocket = money #dont mess with pocket!
        self.table = 0

    def __str__(self):
        return "{} ({}€)".format(self.name, self.pocket-self.table)

    def __repr__(self):
        return self.__str__()

    def payback(self, prize):
        """ receives bet + premium
            or 0 if player lost
        """
        self.table = 0
        self.pocket += prize

# re-implement all the next methods
    def debug_state(self, dealer, players):
        print "Dealer: ", dealer, card.value(dealer.hand)
        for p in players:
            print p.player.name, p.hand, card.value(p.hand)

    def play(self, dealer, players):
        """ Calculates decision to take
            Must be either "h" or "s"
        """
        self.debug_state(dealer, players)
        return raw_input("(h)it or (s)tand  ")

    def bet(self, dealer, players):
        """ Calculates how much to bet

            dealer - state
            players - list of players state
            bet (int value)
        """
        self.debug_state(dealer, players)
        try:
            bet = int(raw_input("bet: "))
        except Exception, e:
            bet = 1
        self.table = bet
        return bet
