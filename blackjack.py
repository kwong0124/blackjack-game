import random
import itertools

# To-do list
# Allow player to decide whether ace counts as 11 or 1 points
# Allow player to place a bet, and return the appropriate amt of $$
# Refactor code
# Add comments and doc strings
# Fix spacing

print('''\nWelcome to the Blackjack game!

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
push, and the player does not win or lose money.\n''')

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
numbers = list(range(2, 11))
royals = ['Ace', 'King', 'Queen', 'Jack']
faces = numbers + royals

deck = []
player_hand = []
dealer_hand = []

deck = list(itertools.product(faces, suits))
random.shuffle(deck)

# Dict to look up points for royal faces
royals_dict = {'Ace': 1, 'King': 10, 'Queen': 10, 'Jack': 10}

def start_playing():
    # Ask user if they want to play the game - player responds with yes or no.
    # If yes, call next function, if no, quit program
    user_input = input('Are you ready to play blackjack? (Y/n): ')
    if user_input.lower() == 'n':
        print('Quitting game... hope to see you soon!\n')
    else:
        print('\nDealing cards...')

def draw_card(card_deck):
    '''draws a card from the shuffled deck'''

    card = card_deck.pop(-1)
    return card

def player():

    player_points = sum_cards(player_hand)

    print('\nYour hand contains {}'.format(player_hand))
    print('\nThe sum of cards in your hand is {}'.format(player_points))

    if player_points < 21:
        player_decision()
    elif player_points == 21:
        print('\nYou\'ve got 21 points! \n\n***Blackjack!*** \n')
    else:
        print('\nThat\'s a bust... Better luck next time!')

def dealer():

    dealer_points = sum_cards(dealer_hand)

    if dealer_points < 21:
        dealer_decision(dealer_points)
    elif dealer_points == 21:
        print('Dealer blackjack!')
    else:
        print('Dealer busts!')


def deal_cards():
    '''deals cards at the beginning of the game'''

    while len(player_hand) < 2:
        player_hand.append(draw_card(deck))
    while len(dealer_hand) < 2:
        dealer_hand.append(draw_card(deck))

    print('\nThe dealer\'s hand is showing {}'.format(dealer_hand[0]))

def player_decision():
    # allows the player decide whether to hit or stay
    player_decision = input('\nWould you like to hit or stand? (h/S): ')

    if player_decision.lower() == 'h':
        new_card = draw_card(deck)
        player_hand.append(new_card)
        print('\nYou drew {}'.format(new_card))
        player()
    else:
        print('\nDealer\'s turn...')

def sum_cards(hand):
    value_list = []
    for card in hand:
        if type(card[0]) == int:
            value_list.append(card[0])
        else:
            value_list.append(royals_dict[card[0]])
    return sum(value_list)

def dealer_decision(points):
    while points < 17:
        new_card = draw_card(deck)
        dealer_hand.append(new_card)
        print('\nThe dealer drew {}.'.format(new_card))
        points = sum_cards(dealer_hand)
    if points == 21:
        print('\n***Dealer blackjack!*** \n\nBetter luck next time...\n')

    else:

        print('\n The dealer\'s hand contains:\n\n {} \n\nThe dealer has {} points\
    ... You have {} points'.format(\
        dealer_hand, sum_cards(dealer_hand), sum_cards(player_hand)))

        if sum_cards(dealer_hand) > 21:
            print('Dealer busts ... you win!')
        elif sum_cards(dealer_hand) < 21 and sum_cards(player_hand) > sum_cards(dealer_hand):
            print('You win!')
        elif sum_cards(dealer_hand) <21 and sum_cards(dealer_hand) > sum_cards(player_hand):
            print('Dealer wins! ... Better luck next time!')
        elif sum_cards(dealer_hand) == sum_cards(player_hand):
            print('It\'s a tie! ... Better luck next time.')
        else:
            print('Dealer blackjack! ... Better luck next time')

def main():

    start_playing()

    deal_cards()

    player()

    if sum_cards(player_hand) < 21:
        while len(dealer_hand) < 2:
            dealer_hand.append(draw_card(deck))
        dealer()

if __name__ == '__main__':
    main()
