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
        print "{:10s}: {:32s} = {}".format("Dealer", dealer.hand, card.value(dealer.hand))
        for p in players:
            print "{:10s}: {:32s} = {}".format(p.player.name, p.hand, card.value(p.hand))

    def play(self, dealer, players):
        """ Calculates decision to take
            Must be either "h", "d" or "s" - Hit, Double down or Stand
            Hit -> player gets an extra card
            Double Down -> player can bet extra money (up to 100% of the initial bet) and a LAST extra card
            Stand -> player does not wish to make any move in the current turn
        """
        self.debug_state(dealer, players)
        return raw_input("(h)it (d)ouble or (s)tand  ")

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
