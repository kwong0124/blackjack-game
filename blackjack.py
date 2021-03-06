import random
import itertools

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
player_points = 0
dealer_points = 0
bank = []

deck = list(itertools.product(faces, suits))

random.shuffle(deck)

royals_dict = {'Ace': 11, 'King': 10, 'Queen': 10, 'Jack': 10}


def start_playing():
    '''Ask user if they want to start playing blackjack'''

    user_input = input('\nAre you ready to play blackjack? (Y/n): ')

    if user_input.lower() == 'n':
        print('\nQuitting game... hope to see you soon!\n')
        quit()
    else:
        pass


def deal_cards():
    '''Deals cards at the beginning of the game'''

    print('\nDealing cards...')

    while len(player_hand) < 2:
        player_hand.append(draw_card(deck))

    while len(dealer_hand) < 2:
        dealer_hand.append(draw_card(deck))

    print('\nThe dealer\'s hand is showing {}'.format(dealer_hand[0]))


def draw_card(card_deck):
    '''Draws a card from the shuffled deck and returns the card'''

    card = card_deck.pop(-1)
    return card


def player(dollar_amount):
    '''Sums the player's points by calling the sum_cards function and
    determines if the player_decision function should be called (i.e. less than
    21 points), elif the player has a blackjack, or else the player busts.'''

    player_points = sum_cards(player_hand)
    print('\nYour hand contains {}'.format(player_hand))
    print('\nThe sum of cards in your hand is {}'.format(player_points))

    if player_points < 21:
        player_decision(dollar_amount)
    elif player_points == 21:
        print('\nYou\'ve got 21 points! \n\n*** Blackjack! *** \n')
        winnings(dollar_amount, 'player')
    else:
        print('\nThat\'s a bust... Better luck next time!')
        winnings(dollar_amount, 'dealer')


def dealer(dollar_amount):
    '''Similar to player player function. Sums the dealer points by calling the
    sum_cards function. Determines if dealer_decision function should be
    called (i.e. dealer has <21 points) elif the dealer has a blackjack, else
    the dealer busts'''

    dealer_points = sum_cards(dealer_hand)

    if dealer_points < 21:
        dealer_decision(dealer_points, dollar_amount)
    elif dealer_points == 21:
        print('\n*** Dealer blackjack! ***')
        winnings(dollar_amount, 'dealer')
    else:
        print('\nDealer busts!')
        winnings(dollar_amount, 'player')


def player_decision(player_bet):
    '''Allows player to decide whether to hit or stay'''

    player_decision = input('\nWould you like to hit or stand? (h/S): ')

    if player_decision.lower() == 'h':
        new_card = draw_card(deck)
        player_hand.append(new_card)
        print('\nYou drew {}'.format(new_card))
        player(player_bet)
    else:
        print('\nDealer\'s turn...')


def dealer_decision(points, player_bet):
    '''Draws cards until the dealer hand point total is greater than 17, has a
    blackjack or busts (whichever comes first). Determines who wins by comparing
    dealer_hand and player_hand'''

    while points < 17:
        new_card = draw_card(deck)
        dealer_hand.append(new_card)
        print('\nThe dealer drew {}.'.format(new_card))
        points = sum_cards(dealer_hand)

    if points == 21:
        print('\n*** Dealer blackjack! *** \n\nBetter luck next time...\n')
        winnings(player_bet, 'dealer')
    else:
        print('\n The dealer\'s hand contains:\n\n {} \n\nThe dealer has {} points\
... You have {} points'.format(\
        dealer_hand, sum_cards(dealer_hand), sum_cards(player_hand)))

        if sum_cards(dealer_hand) > 21:
            print('\nDealer busts ... you win!')
            winnings(player_bet, 'player')
        elif sum_cards(dealer_hand) < 21 and sum_cards(player_hand) > sum_cards(dealer_hand):
            print('\nYou win!')
            winnings(player_bet, 'player')
        elif sum_cards(dealer_hand) <21 and sum_cards(dealer_hand) > sum_cards(player_hand):
            print('\nDealer wins! ... Better luck next time!')
            winnings(player_bet, 'dealer')
        elif sum_cards(dealer_hand) == sum_cards(player_hand):
            print('\nIt\'s a tie! ... Better luck next time.')
            winnings(player_bet, 'tie')
        else:
            print('\nDealer blackjack! ... Better luck next time')
            winnings(player_bet, 'dealer')


def sum_cards(hand):
    '''Takes a hand of cards and returns the point value of cards in the hand'''

    value_list = []
    aces = sum(card.count('Ace') for card in hand)

    for card in hand:

        if type(card[0]) == int:
            value_list.append(card[0])
        else:
            value_list.append(royals_dict[card[0]])

        points = sum(value_list)

    while points > 21 and aces:
        points = points - 10
        aces -= 1

    return points


def winnings(bet_amount, winner):
    '''Calculates amount of money awarded to the player or casino'''

    cashflow = 0
    winner_take_home = int(bet_amount) * 2
    bet_amount = int(bet_amount)

    if winner == 'dealer':
        cashflow = cashflow - bet_amount
        print('\nSorry - you lost ${}.00'.format(bet_amount))
    elif winner == 'player':
        cashflow = cashflow + winner_take_home
        print('\nReturning ${0}.00 to your bank.'.format(winner_take_home))
    else:
        cashflow = cashflow + bet_amount
        print('\nYou get to keep your bet of ${}.00'.format(bet_amount))

    return bank_update(cashflow)


def bank_update(change_in_bank):
    '''updates the bank variable with new cashflow'''

    bank.append(change_in_bank)
    print('\nYou now have ${}.00 in your bank.'.format(sum(bank)))

def play_again():
    '''ask the user if he/she wants to play again. If yes, call main function,
    if no, exit the game'''

    response = input('\nWould you like to play again? (Y/n): ')

    if response.lower() == 'n':
        if sum(bank) > 0:
            print('\nThanks for playing Blackjack game! Your winnings of \n\
${}.00 will be returned to you.\n'.format(sum(bank)))
        elif sum(bank) < 0:
            print('\nThanks for playing the Blackjack game! You owe ${}.00.\n\
Please pay on your way out.\n'.format(abs(sum(bank))))
        else:
            print('Thanks for playing Blackjack game! You have $0.00 in your \n\
bank.\n')
    else:
        print('\nStarting new game...Good luck!')
        main()

def main():

    start_playing()

    bet = float(input('\nPlease enter your bet (in $): '))

    deal_cards()

    player(bet)

    if sum_cards(player_hand) < 21:

        while len(dealer_hand) < 2:
            dealer_hand.append(draw_card(deck))

        dealer(bet)

    while len(player_hand) > 0:
        player_hand.pop()

    while len(dealer_hand) > 0:
        dealer_hand.pop()

    play_again()

if __name__ == '__main__':

    main()
