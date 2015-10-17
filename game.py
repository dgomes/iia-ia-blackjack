#encoding: utf8
__author__ = 'Diogo Gomes'
__email__ = 'dgomes@ua.pt'
__license__ = "GPL"
__version__ = "0.1"

import copy
import card
from dealer import Dealer
from player import Player 

BET_MULTIPLIER = 2

class Game(object):
    class PlayerState():
        def __init__(self, p):
            print(chr(27) + "[2J")
            self.player = p
            self.bet = 0
            self.hand = []
            self.bust = False
        def copy(self):
            return copy.deepcopy(self)
        def __str__(self):
            if isinstance(self.player, Dealer):
                return "{}".format(self.hand)
            return "{} ({}€)".format(self.hand, self.bet)
        def __repr__(self):
            return "{}".format(self.player.name)
        def hide_card(self):
            h = self.copy()
            h.hand = h.hand[1:]
            return h 

    def __init__(self, players, shoe_size=4):
        self.shoe = card.Shoe(shoe_size)
        self.shoe.shuffle()
        self.state = [self.PlayerState(Dealer())] + [self.PlayerState(p) for p in players]
        
        self.state[0].hand += self.shoe.deal_cards(2)
        self.state[1].hand += self.shoe.deal_cards(2)
        
        self.done = False

    def __str__(self):
        return (\
        "{:^"+str(30)+"}\n"\
        "╔═══════════════════════════════╗\n"\
        "{:^45}\n"\
        "                         \n"\
        "                         \n"\
        "                         \n"\
        "                         \n"\
        "                         \n"\
        "{:^45}\n"\
        "╚═══════════════════════════════╝\n"\
        "{:^30}\n"\
        ).format(self.state[0].player.name, self.state[0].hand if self.done else ["**"]+self.state[0].hide_card().hand, self.state[1], self.state[1].player) + \
        "\nDealer: {}\n"\
        "Player: {}\n".format(card.value(self.state[0].hand), card.value(self.state[1].hand))


    def deal(self, num):
        return self.shoe.deal_cards(1)

    def take_bets(self):
        print(self)
        for p in self.state[1:]:
            bet = 0
            while bet <=0:
                bet = p.player.bet(self.state[0].hide_card(), self.state[1:])
            p.bet = bet

    def loop(self):
        hits = 2 
        while hits != 0 and not self.done:
            hits = 0
            for p in self.state:
                if p.bust:  #skip bust players
                    continue    

                print("TURN: " + p.player.name)
                print(self)
                action = ""
                while action not in ["h", "s"]:
                    if isinstance(p.player, Dealer):
                        action = p.player.play(self.state[0], self.state[1:])
                    else:
                        action = p.player.play(self.state[0].hide_card(), self.state[1:])

                if action == "h":
                    p.hand+=self.deal(1)
                    hits +=1
                
                if card.value(p.hand) > 21:
                    p.bust = True    
                    if isinstance(p.player, Dealer):
                        self.done = True
                        break
                if card.value(p.hand) == 21:
                    self.done = True
                    break

        self.done = True
        return [p for p in self.state if 
            not isinstance(p.player, Dealer) and 
            not p.bust and 
            (card.value(p.hand) >= card.value(self.state[0].hand) or self.state[0].bust)
            ]

    def payback(self, winners):
        for p in self.state[1:]:
            if p in winners and card.value(self.state[0].hand) == card.value(p.hand):
                p.player.payback(p.bet)  #bet is returned
            elif p in winners:
                p.player.payback(p.bet*BET_MULTIPLIER)
            else:
                p.player.payback(0) #this means the player lost

    def run(self):
        self.take_bets()
        winners = self.loop()
        self.payback(winners)
        print(self)
        print("🏆    Winners: "+str(winners))

