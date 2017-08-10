import deck
import black_jack_player

class BlackJack(object):
    def __init__(self):
        self.player = self.create_player('Player')
        self.dealer = Dealer()

    def create_player(self, title):
        name = input("Enter {}'s name: ".format(title))
        return Player(name)

    def deal_to_player(self):
        card1, card2 = self.dealer.draw_card(), self.dealer.draw_card()
        return "{} is dealt {} and {}.".format(card1, card2)

    def hit_or_stay(self):
        return input("Would you like to [h]it or [s]tay?: ")
