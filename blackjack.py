import random
import itertools

# To-do list


#class Card:
#    def __init__(self, face, suit):
#        self.face = face
#        self.suit = suit
#        self.card = face + 'of' + suit

num_decks = 1

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
numbers = list(range(2, 11))
royals = ['Ace', 'King', 'Queen', 'Jack']
faces = numbers + royals
deck = []
player_hand = []
dealer_hand = []

deck = list(itertools.product(faces, suits))

#shuffle the deck
random.shuffle(deck)

royals_dict = {'Ace': 1, 'King': 10, 'Queen': 10, 'Jack': 10}

print('''
Welcome to the Blackjack game!

The objective of the game is to beat the dealer in one of the following ways:
- Get 21 points on the player's first two cards, without a dealer blackjack
- Reach final score higher than the dealer without exceeding 21
- Let the dealer draw additional cards until he exceeds 21

Face cards are ten points. An ace can be either one or eleven points.
All other cards are counted as the numeric value shown on the card. In each
round, the player can decide whether to "hit" or "stand". If the player chooses
to hit, the he or she is dealt another card.
If they player chooses to stand, then it becomes the dealer's turn.

Scoring higher than 21 (i.e. "busting"), results in a loss.
The dealer must hit until the cards total 17 or more points.
The player may win by having any score less than 21 if the dealer busts.
If the player and the dealer end with the same card value, this is called a
push, and the player does not win or lose money.

    ''')

def start_playing():
    # Ask user if they want to play the game - player responds with yes or no.
    # If yes, call next function, if no, quit program
    user_input = input('Are you ready to play blackjack? (Y/n): ')
    if user_input.lower() == 'n':
        print('Quitting game... hope to see you soon!\n')
    else:
        print('\nDealing cards...\n')

def draw_card(card_deck):
    '''draws a card'''

    card = card_deck.pop(-1)
    return card

def player():

    print('\nYour hand contains {}\n'.format(player_hand))
    print('\nThe sum of cards in your hand is {}'.format(sum_cards(player_hand)))

def dealer():

    print('\nThe dealer\'s hand is showing {}\n'.format(dealer_hand[0]))

    player_decision()


def player_decision():
    # allows the player decide whether to hit or stay
    player_decision = input('Would you like to hit or stand? (h/S): ')

    if player_decision.lower() == 'h':
        new_card = draw_card(deck)
        player_hand.append(new_card)
        print('\nYou drew {}\n'.format(new_card))
        print('Your hand now contains {}\n'.format(player_hand))
    else:
        print('\nDealer\'s turn...\n')

def sum_cards(hand):
    value_list = []
    for card in hand:
        if type(card[0]) == int:
            value_list.append(card[0])
        else:
            value_list.append(royals_dict[card[0]])
    return sum(value_list)



def dealer_decision(arg):
    #determines whether the dealer hits or stays
    pass

def main():

    start_playing()

    while len(player_hand) < 2:
        player_hand.append(draw_card(deck))

    player()

    while len(dealer_hand) < 2:
        dealer_hand.append(draw_card(deck))

    dealer()

if __name__ == '__main__':
    main()
