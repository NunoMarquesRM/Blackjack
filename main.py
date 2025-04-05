"""
Blackjack Game Implementation
This is a simple command-line implementation of the Blackjack card game.
The game follows standard Blackjack rules where players try to get as close to 21 as possible
without going over, while competing against a computer dealer.
"""

import random
from art import logo

def deal_card():
    """
    Deals a random card from a standard deck.
    Returns:
        int: A card value (1-11, where 11 represents Ace)
    """
    # 11 represents Ace, 10 represents face cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    Calculates the score of a hand of cards, handling Aces appropriately.
    
    Args:
        cards (list): List of card values in the hand
        
    Returns:
        int: The calculated score of the hand
    """
    # Convert Ace from 11 to 1 if score would exceed 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    # Return 0 for Blackjack (natural 21 with first two cards)
    if len(cards) == 2 and sum(cards) > 21:
        return 0

    return sum(cards)

def compare21(your_score, pc_score):
    """
    Compares scores to determine the winner when a player has 21.
    
    Args:
        your_score (int): Player's score
        pc_score (int): Computer's score
        
    Returns:
        str: Message indicating the game result
    """
    if your_score == 21:
        return "Win with a Blackjack!"
    if pc_score == 21:
        return "Lose, opponent has Blackjack!"
    # your_score > 21:
    return "You went over. You lose!"

def final_hand(your_cards, your_score, pc_cards, pc_score, string_text):
    """
    Displays the final state of the game.
    
    Args:
        your_cards (list): Player's cards
        your_score (int): Player's score
        pc_cards (list): Computer's cards
        pc_score (int): Computer's score
        string_text (str): Result message to display
    """
    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print(f"Computer's final hand: {pc_cards}, final score: {pc_score}")
    print(string_text)

def play_game():
    """
    Main game loop that handles the Blackjack game logic.
    Manages dealing cards, player decisions, and determining the winner.
    """
    print(logo)
    # Initial deal
    your_cards = [deal_card(), deal_card()]
    your_score = calculate_score(your_cards)
    pc_cards = [deal_card(), deal_card()]
    pc_score = calculate_score(pc_cards)

    game_isRunning = True
    while game_isRunning:
        # Check for immediate game end conditions
        if your_score >= 21 or pc_score == 21:
            final_hand(your_cards, your_score, pc_cards, pc_score, compare21(your_score, pc_score))
            game_isRunning = False
        else:
            # Display current game state (your_score < 21)
            print(f"    Your cards: {your_cards}, current score: {your_score}")
            print(f"    Computer's first card: {pc_cards[0]}")
            your_choice = input("Type 'y' to get another card, type 'n' to pass: ")

            if your_choice.lower() == 'y' or 'n':
                if your_choice.lower() == 'y':
                    # Player hits
                    your_cards.append(deal_card())
                    your_score = calculate_score(your_cards)
                else:
                    # Player stands, computer plays
                    while pc_score < 17:
                        pc_cards.append(deal_card())
                        pc_score = calculate_score(pc_cards)

                    # Determine winner
                    if pc_score > 21:
                        final_hand(your_cards, your_score, pc_cards, pc_score, "Opponent went over. You win!")
                    else:
                        if your_score == pc_score:
                            final_hand(your_cards, your_score, pc_cards, pc_score, "Draw!")
                        elif your_score > pc_score:
                            final_hand(your_cards, your_score, pc_cards, pc_score, "You Win!")
                        else:
                            final_hand(your_cards, your_score, pc_cards, pc_score, "Opponent Wins!")
                    game_isRunning = False
            else:
                print("Incorrect input!")

# Game loop
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play.lower() == 'y':
    # Clear screen between games
    print("\n" * 20)
    play_game()
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

print("Bye!")