# Blackjack Game

A command-line implementation of the classic Blackjack card game, where players compete against a computer dealer to get as close to 21 as possible without going over.

## Features

- 🎮 Interactive command-line interface
- 🎲 Standard Blackjack rules implementation
- 👤 Player vs Computer dealer gameplay
- 🎯 Automatic score calculation with Ace handling (1 or 11)
- 🏆 Multiple game outcomes:
  - Blackjack (natural 21)
  - Win
  - Lose
  - Draw
- 🔄 Multiple rounds support
- 🎨 ASCII art logo display

## Game Rules

1. The goal is to get a hand value closer to 21 than the dealer without going over
2. Number cards (2-10) are worth their face value
3. Face cards (Jack, Queen, King) are worth 10
4. Ace can be worth 1 or 11, whichever is more favorable
5. The dealer must hit on 16 and below, stand on 17 and above
6. A natural Blackjack (first two cards totaling 21) beats a regular 21

## How to Play

1. Start the game by running `python main.py`
2. Choose whether to play a game by typing 'y' or 'n'
3. During the game:
   - View your cards and current score
   - See the dealer's first card
   - Choose to:
     - Hit ('y'): Receive another card
     - Stand ('n'): End your turn and let the dealer play
4. The game will automatically determine the winner based on standard Blackjack rules
5. Choose to play another round or exit the game

## Requirements

- Python 3.x
- No additional packages required (uses only Python standard library)

## File Structure

- `main.py`: Contains the main game logic and implementation
- `art.py`: Contains the ASCII art logo for the game

## Game Outcomes

- **Blackjack**: Win with a natural 21 (first two cards)
- **Win**: Your hand is closer to 21 than the dealer's
- **Lose**: 
  - Your hand exceeds 21
  - Dealer has a better hand
  - Dealer has Blackjack
- **Draw**: Your hand equals the dealer's hand

## Example Game Flow

```
Do you want to play a game of Blackjack? Type 'y' or 'n': y

    Your cards: [7, 10], current score: 17
    Computer's first card: 6
Type 'y' to get another card, type 'n' to pass: n

Your final hand: [7, 10], final score: 17
Computer's final hand: [6, 8, 4], final score: 18
Opponent Wins! 