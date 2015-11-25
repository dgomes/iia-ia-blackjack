#encoding: utf8
__author__ = 'Diogo Gomes'
__email__ = 'dgomes@ua.pt'
__license__ = "GPL"
__version__ = "0.1"

from card import Card
from shoe import Shoe

class TestShoe(Shoe):
    def __init__(self, cards=[]):
        self.cards = cards 

    def shuffle(self):
        pass

    def sort(self):
        pass

if __name__ == '__main__':
    shoe = TestShoe([Card(0,1), Card(1,11)])
    shoe.shuffle()

    print shoe.deal_cards(2)

