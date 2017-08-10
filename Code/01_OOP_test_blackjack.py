import nose.tools as n
from deck import Card
from blackjack import BlackJack
from black_jack_player import Player
from black_jack_player import Dealer

def test_player_init():
    player1 = Player('Ben')
    dealer1 = Dealer()
    n.assert_equal(player1.bankroll, 0)
    n.assert_equal(player1.hand, [])
    n.assert_equal(len(dealer1.deck), 52 )

def test_deal_to_player():
    dealer = Dealer()
    
    n.assert_equal(type(dealer.draw_card()), str)




# def test_player_name():

'''
def test_player_receive_play():
    player = Player("name")
    card = Card("J", "c")
    player.receive_card(card)
    n.assert_equal(len(player), 1)
    n.assert_equal(player.play_card(), card)
    n.assert_equal(len(player), 0)

def test_war_deal():
    game = War(human=False)
    n.assert_equal(len(game.player1), 26)
    n.assert_equal(len(game.player2), 26)

def test_play_round():
    game = War(human=False)
    game.play_round()
    n.assert_equal(len(game.player1) + len(game.player2), 52)

def test_play_game():
    game = War(human=False)
    game.play_game()
    n.assert_equal(len(game.player1) + len(game.player2) + len(game.pot), 52)
    n.assert_is_not_none(game.winner)
    if game.player1.name == game.winner:
        n.assert_equal(len(game.player2), 0)
    else:
        n.assert_equal(len(game.player1), 0)

def test_war_size():
    game = War(war_size=5, human=False)
    game.play_round() #Play first to shuffle hand
    game.war()
    n.assert_equal(len(game.pot), 10)

def test_play_two_of_three():
    game = War(human=False)
    #There should be a dictionary that tracks win counts.
    n.assert_equal(max(game.win_counts.values()), 0)
    game.play_two_of_three()
    n.assert_equal(max(game.win_counts.values()), 2)
    #Make sure you don't get too many cards!
    n.assert_equal(len(game.player1) + len(game.player2) + len(game.pot), 52)

'''
