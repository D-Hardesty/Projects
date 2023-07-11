import random
import art

# Unlimited cards
# card dictionary
card_dict = {
    "A": 11,  # Ace == 1 or 11.
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10}


dealer = []
player = []
player_value = []
dealer_value = []


def game_start():
    print(art.logo)
    print("The dealer shuffles 100 decks together with their massive hands.\n")
    # dealing = True
    # card_num = 0
    show = 0
    clear_values()
    for _ in range(2):
        hit("dealer", 0, show)
        hit("player", 0, show)
        show += 1
    is_blackjack()
    game_in_play()


def is_blackjack():
    if sum(player_value) == 21 and sum(dealer_value) == 21:
        print(f"Uh this usually never happens. You ({player}) and the dealer({dealer}) both got a BLACKJACK! ")
        play_again()
    elif sum(player_value) == 21:
        print(f"BLACKJACK!!!! {player}\n You win! \n")
        play_again()
    elif sum(dealer_value) == 21:
        print(f"Dealer gets a BLACKJACK!!!! {dealer}\n You Lose!\n")
        play_again()


def clear_values():
    player_value.clear()
    dealer_value.clear()
    dealer.clear()
    player.clear()


# Gameplay loop, player hits or stays, dealer hits if hand value is less than 17
def game_in_play():
    visible_dealer = dealer.copy()
    visible_dealer.pop(0)
    # Dealer's Hand visible to player
    print(f"Dealer's hand: {visible_dealer}")
    # Player's hand
    print(f"Your hand: {player}\n")

    action = input("Do you want to 'hit' or 'stay'? ").lower()

    if action == "hit":
        print("You hit!")
        hit("player", 0, 1)
    elif action == "stay":
        stay()
    else:
        print("Please pick a valid action.")
        game_in_play()

    if sum(dealer_value) < 17:
        print("Dealer hits!")
        hit("dealer", 0, 1)
    else:
        print("Dealer stays!")

    game_in_play()


# calculates and informs the player of their hand value and calls player_out()
def stay():
    print(f"You stay with a hand value of {sum(player_value)}: {player}\n")
    print(f"The dealer flips their cards over.")
    player_out()


# continues the game if the player chooses to stay. Dealer plays out the rest of the game.
def player_out():
    print(f"Dealer's Hand: {dealer}\n")
    if sum(dealer_value) < 17:
        print("Dealer hits")
        hit("dealer", 1, 1)
    else:
        print("Dealer stays!")
        end_of_game()


def hit(p, v, s):
    """p == player hitting, v == if the player is still in the game, s == if the dealer's card should be shown."""
    if p == "player":
        # picks a random key from the card dictionary and adds it to the player's hand and their hand value.
        deal_card("p", 0)
        hand_value = sum(player_value)
        if hand_value > 21:
            if "A" in player:
                ace_location = player.index("A")
                player[ace_location] = 1
                player_value[ace_location] = 1
                game_in_play()
            bust("player", sum(player_value))
    else:
        deal_card("d", s)
        hand_value = sum(dealer_value)
        if hand_value > 21:
            if "A" in dealer:
                ace_location = dealer.index("A")
                dealer[ace_location] = 1
                dealer_value[ace_location] = 1
                game_in_play()
            bust("dealer", sum(dealer_value))
        if v == 1:
            player_out()


def deal_card(p, s):
    if p == "p":
        player_card = random.choice(list(card_dict))
        player.append(player_card)
        player_value.append(card_dict[player_card])
        print(f"You are delt a {player_card}.\n")
    elif p == "d":
        dealer_card = random.choice(list(card_dict))
        if s > 0:
            print(f"Dealer deals themselves a {dealer_card}.\n")
        dealer.append(dealer_card)
        dealer_value.append(card_dict[dealer_card])


def end_of_game():
    p_value = sum(player_value)
    d_value = sum(dealer_value)

    if p_value > d_value:
        print(f"You won with a value of {p_value}({player}) to the dealer's {d_value} ({dealer}).\n")
        play_again()
    elif p_value == d_value:
        print(f"You tied the dealer ({dealer}) with a value of {p_value} ({player}).\n")
        play_again()
    else:
        print(f"You lose with a value of {p_value} ({player}) to the dealer's {d_value} ({dealer})\n")
        play_again()


# Declares a winner if a player busts.
def bust(p, v):
    """p == which player busted, v == hand value at time of bust"""
    if p == "player":
        print(f"You busted ({player}) with a hand value of {v}! You Lose!\n")
    else:
        print(f"The dealer busted ({dealer}) with a hand value of {v}! You win!\n")
    play_again()


# Asks if the user wants to play another game and restarts the game or exits the program.
def play_again():
    again = input("Do you want to play again? 'Y' or 'N' \n").lower()
    if again == "y":
        game_start()
    elif again != "n":
        print("Please, pick a valid option!")
        play_again()
    print("\nThanks for playing! Bye!!!")
    exit()


game_start()
