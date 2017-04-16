# black jack card game

def directions():
    print('''
    Welcome to the Blackjack game!

    The objective of the game is to beat the dealer in one of the following ways:
    - Get 21 points on the player's first two cards, without a dealer blackjack
    - Reach final score higher than the dealer without exceeding 21
    - Let the dealer draw additional cards until he exceeds 21

        ''')
    print('''
    The player(s) are dealt a two-card hand and add together the value of their
    cards. Face cards are ten points. An ace is either a one or eleven points.
    All other cards are counted as the numeric value shown on the card. After
    the players are shown the first two cards, they have the option to take a
    "hit" (i.e. take an additional card). In each round, the player or the dealer
    wins by having a score of 21 or by having the higher score that is <21.
    Scoring higher than 21 (i.e. "busting"), results in a loss. A player may win
    by having a score less than 21 if the dealer busts.

    The dealer must hit until the cards total 17 or more points. If the player
    and the dealer end with the same card value, this is called a push, and the
    player does not win or lose money. 
    ''')
