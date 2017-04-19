import random
import itertools

# questions
# why does random.shuffle(deck) return None?

# To-do list


class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        self.card = face + 'of' + suit

num_decks = 1

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
numbers = list(range(2, 11))
royals = ['Ace', 'King', 'Queen', 'Jack']
faces = numbers + royals
deck = []
player_hand = []
dealer_hand = []

for suit in suits:
    for face in faces:
        deck.append((face, suit))

random.shuffle(deck)

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
"hit" (i.e. take an additional card). In each round, the player or the
dealer wins by having a score of 21 or by having the higher score that is
<21. Scoring higher than 21 (i.e. "busting"), results in a loss. A player
may win by having a score less than 21 if the dealer busts.

The dealer must hit until the cards total 17 or more points. If the player
and the dealer end with the same card value, this is called a push, and the
player does not win or lose money.

''')

def start_playing():
    # ask user if they want to play the game
    # user responds with yes or no
    # if yes, call next function, if no, quit program
    user_input = input('Are you ready to play blackjack? (Y/n): ')
    if user_input.lower() == 'n':
        print('Quitting game... hope to see you soon!')
    else:
        print('Dealing cards...')

def draw_card(card_deck):
    '''draws a card'''

    card = card_deck.pop(-1)
    return card

def player():
    while len(player_hand) < 2:
        player_hand.append(draw_card(deck))

    print('Your hand contains {}'.format(player_hand))

    dealer()

def dealer():
    while len(dealer_hand) < 2:
        dealer_hand.append(draw_card(deck))

    print('The dealer\'s hand is showing {}'.format(dealer_hand[0]))


def player_decision(arg):
    # allows the player decide whether to hit or stay
    pass

def dealer_decision(arg):
    #determines whether the dealer hits or stays
    pass

def main():
    player()

if __name__ == '__main__':
    main()
