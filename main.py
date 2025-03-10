import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    if len(cards) == 2 and sum(cards) > 21:
        return 0

    return sum(cards)

def compare21(your_score,pc_score):
    if your_score == 21:
        return "Win with a Blackjack!"
    if pc_score == 21:
        return "Lose, opponent has Blackjack!"
    # your_score > 21:
    return "You went over. You lose!"

def final_hand(your_cards,your_score,pc_cards,pc_score, string_text):
    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print(f"Computer's final hand: {pc_cards}, final score: {pc_score}")
    print(string_text)

def play_game():
    print(logo)
    your_cards = [deal_card(), deal_card()]
    your_score = calculate_score(your_cards)
    pc_cards = [deal_card(),deal_card()]
    pc_score = calculate_score(pc_cards)

    game_isRunning = True
    while game_isRunning:
        if your_score >= 21 or pc_score == 21:
            final_hand(your_cards, your_score, pc_cards, pc_score, compare21(your_score,pc_score))
            game_isRunning = False
        else:
            #your_score < 21:
            print(f"    Your cards: {your_cards}, current score: {your_score}")
            print(f"    Computer's first card: {pc_cards[0]}")
            your_choice = input("Type 'y' to get another card, type 'n' to pass: ")

            if your_choice.lower() == 'y' or 'n':
                if your_choice.lower() == 'y':
                    your_cards.append(deal_card())
                    your_score = calculate_score(your_cards)
                else:
                    while pc_score < 17:
                        pc_cards.append(deal_card())
                        pc_score = calculate_score(pc_cards)

                    if pc_score > 21:
                        final_hand(your_cards, your_score, pc_cards, pc_score, "Opponent went over. You win!")
                    else:
                        if your_score == pc_score:
                            final_hand(your_cards, your_score, pc_cards, pc_score,"Draw!")
                        elif your_score > pc_score:
                            final_hand(your_cards, your_score, pc_cards, pc_score,"You Win!")
                        else:
                            final_hand(your_cards, your_score, pc_cards, pc_score,"Opponent Wins!")
                    game_isRunning = False
            else:
                print("Incorrect input!")


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play.lower() == 'y':
    print("\n" * 20)
    play_game()
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

print("Bye!")