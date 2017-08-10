import random
from deck import Deck

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bankroll = 0


    def receive_card(self, card):
        self.hand.append(card)

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def add_subtract_bankroll(self, num):
        return self.bankroll + num

    def __str__(self):
        return self.hand

    def __repr__(self):
        return self.name


class Dealer(Deck):

    def __init__(self):
        self.deck = self.new_deck()

    def new_deck(self):
        deck = Deck()
        deck.shuffle()
        return deck
