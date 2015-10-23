#encoding: utf8
__author__ = 'Diogo Gomes'
__email__ = 'dgomes@ua.pt'
__license__ = "GPL"
__version__ = "0.1"


import random

class Card(object):
    suit_names = ["♠️", "♣️", "♦️", "♥️"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=1):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '{}{} '.format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __repr__(self):
        return self.__str__()

    def value(self):
        return self.rank if self.rank < 10 else 10

    def is_ace(self):
        if self.rank == 1:
            return True
        return False
    def is_ten(self):
        if self.rank >= 10:
            return True
        return False

class Shoe(object):
    #Represents one or more decks of cards use to
    #take cards for players and dealer

    def __init__(self, number_decks=1):
        self.cards = []
        for i in range(number_decks):
            self.cards += [Card(suit, rank) for suit in range(4) for rank in range(1,14)]

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def deal_cards(self, num):
        """Moves the given number of cards from the deck

        num: integer number of cards to move
        """
        deal = []
        for i in range(num):
            deal.append(self.pop_card())
        return deal

def value(hand):    #TODO as deve valer 1 ou 11 conforme der mais jeito!
    v = sum([c.value() for c in hand]) 
    if len([c for c in hand if c.is_ace()]) > 0 and v <= 11: #if there is an Ace and we don't bust by take the Ace as an eleven
        return v+10 
    return v

def blackjack(hand):
    if len(hand) == 2 and hand[0].is_ace() and hand[1].is_ten():
        return True
    if len(hand) == 2 and hand[1].is_ace() and hand[0].is_ten():
        return True
    return False
    
if __name__ == '__main__':
    shoe = Shoe()
    shoe.shuffle()

    print shoe.deal_cards(2)

