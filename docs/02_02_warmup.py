'''
Let's say we play a game where I keep flipping a coin until I get heads.
If the first time I get heads is on the nth coin,
then I pay you 2n-1 dollars. How much would you pay me to play
this game for us to break even in the long term? Show your work.

Write a program to simulate the game and verify that your answer is correct.
'''

'''Use geometric distribution'''

''' p * pay'''


def run_expected_value(num_flips,pay,prob_heads, num_trials):
    p = prob_heads
    payout = 2*pay - 1
    num_flips = num_flips
    outcome = []


    for i in range(num_trials):
        outcome.append((p * payout)*num_flips)

    return "mean payout: {}".format(round(sum(outcome)/len(outcome),2))

if __name__ == '__main__':
    print(run_expected_value(10, 1, .5, 10000))
