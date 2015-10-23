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
            self.player = p
            self.bet = 0
            self.hand = []
            self.bust = False
            self.done = False
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
        def take_bet(self, state):
            bet = 0
            while bet <=0 or (bet>self.bet and self.bet!=0):      #bets can't be 0 nor can't they be more than double the existing bet
                bet = self.player.bet(state[0].hide_card(), state[1:])
            self.bet += bet

    def __init__(self, players, shoe_size=4, debug=False, verbose=True):
        if verbose:
    #       print(chr(27) + "[2J")
            print("-"*80)
        self.verbose = verbose
        self.debug = debug
        self.shoe = card.Shoe(shoe_size)
        self.shoe.shuffle()
        self.state = [self.PlayerState(Dealer())] + [self.PlayerState(p) for p in players]

        self.state[0].hand += self.shoe.deal_cards(2)
        for p in self.state[1:]:
            p.hand += self.shoe.deal_cards(2)

        self.done = False

    def str_players_hands(self):
        o = ""
        for p in self.state[1:]:
            o+="{:^45}".format(p)
        return o

    def str_players_names(self):
        o = ""
        for p in self.state[1:]:
            o+="{:^35}".format(p.player)
        return o

    def __str__(self):
        return (\
        "{:^30}\n"\
        "╔"+"═══════════════════════════════"*(len(self.state)-1)+"╗\n"\
        "{:^45}\n"\
        "                         \n"\
        "                         \n"\
        "                         \n"\
        "                         \n"\
        "                         \n"\
        "{}\n"\
        "╚"+"═══════════════════════════════"*(len(self.state)-1)+"╝\n"\
        "{}\n"\
        ).format(self.state[0].player.name, self.state[0].hand if self.done else ["**"]+self.state[0].hide_card().hand, self.str_players_hands(), self.str_players_names())

    def deal(self, num):
        return self.shoe.deal_cards(1)

    def take_bets(self):
        if self.debug:
            print(self)
        for p in self.state[1:]:
            p.take_bet(self.state)

    def loop(self):
        turn = 0
        while not self.done:
            turn += 1
            hits = 0
            for p in self.state:
                if p.bust or p.done or card.value(p.hand) == 21:  #skip bust players, players who have double down and players who already have blackjack!
                    continue

                if self.debug:
                    print("TURN {}: {}".format(turn, p.player.name))
                    print(self)
                action = ""
                while action not in ["h", "s", "d"]:
                    if isinstance(p.player, Dealer):
                        action = p.player.play(self.state[0], self.state[1:])
                    else:
                        action = p.player.play(self.state[0].hide_card(), self.state[1:])
                    if action == "d" and turn != 1:
                        action = ""
                
                if action == "d":
                    p.take_bet(self.state)
                    p.done = True

                if action in ["h", "d"]:
                    p.hand+=self.deal(1)
                    hits +=1

                if card.value(p.hand) >= 21:
                    if card.value(p.hand) > 21:
                        p.bust = True
                    if isinstance(p.player, Dealer):
                        self.done = True
            if hits == 0:
                self.done = True

        self.done = True
        return [p for p in self.state if
            not isinstance(p.player, Dealer) and
            not p.bust and
            (card.value(p.hand) >= card.value(self.state[0].hand) or self.state[0].bust)
            ]

    def payback(self, winners):
        for p in self.state[1:]:
            if p in winners and card.value(self.state[0].hand) == card.value(p.hand):
                p.player.payback(0)  #bet is returned
            elif p in winners:
                p.player.payback(-p.bet + p.bet*BET_MULTIPLIER)
            else:
                p.player.payback(-p.bet) #this means the player lost

    def run(self):
        self.take_bets()
        winners = self.loop()
        self.payback(winners)
        if self.verbose:
            print(self)
            print("🏆    Winners: "+str(winners))

