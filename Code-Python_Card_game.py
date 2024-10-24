import random

# Constants for the cards used in the game
SUITS = ['♠', '♢', '♡', '♣']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Class representing a playing card
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"


# Class representing a player's hand
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def display_hand(self):
        for card in self.cards:
            print(card, end=" ")
        print()


# Class representing a player
class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand


# Class representing the Rummy game
class RummyGame:
    def __init__(self):
        self.deck = []
        self.players = []
        self.discard_pile = []

    def create_deck(self):
        self.deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_cards(self):
        for _ in range(7):
            for player in self.players:
                card = self.deck.pop(0)
                player.hand.add_card(card)

    def display_discard_pile(self):
        if len(self.discard_pile) > 0:
            top_card = self.discard_pile[-1]
            print("Top card in discard pile:", top_card)
        else:
            print("Discard pile is empty.")

    def draw_card(self):
        if len(self.deck) > 0:
            card = self.deck.pop(0)
            return card
        else:
            return None

    def discard_card(self, player, card):
        player.hand.remove_card(card)
        self.discard_pile.append(card)

    def check_win(self, player):
        if len(player.hand.cards) == 0:
            return True
        return False

    def play(self):
        print("Welcome to Rummy Game!")

        # Create and shuffle the deck
        self.create_deck()
        self.shuffle_deck()

        # Create players
        num_players = 2
        for i in range(num_players):
            name = input(f"Enter the name of player {i+1}: ")
            hand = Hand()
            self.players.append(Player(name, hand))

        # Deal initial cards
        self.deal_cards()

        # Game loop
        game_over = False
        current_player_index = 0
        while not game_over:
            current_player = self.players[current_player_index]

            print("\n---", current_player.name, "'s turn ---")
            print("Your hand:")
            current_player.hand.display_hand()
            self.display_discard_pile()

            # Draw a card
            print("Draw a card (D) or pick from discard pile (P)?")
            action = input("Enter your action: ").upper()

            if action == 'D':
                card = self.draw_card()
                if card:
                    current_player.hand.add_card(card)
                    print("You drew:", card)
                else:
                    print("No cards left in the deck.")
            elif action == 'P':
                top_card = self.discard_pile[-1] if self.discard_pile else None
                if top_card:
                    print("Top card in discard pile:", top_card)
                    card_index = int(input("Enter the index of the card to pick: ")) - 1
                    if 0 <= card_index < len(current_player.hand.cards):
                        picked_card = current_player.hand.cards[card_index]
                        current_player.hand.remove_card(picked_card)
                        self.discard_pile.append(picked_card)
                        print("You picked:", picked_card)
                    else:
                        print("Invalid card index.")
                else:
                    print("No cards in the discard pile.")

            # Check if the player has won
            if self.check_win(current_player):
                game_over = True
                print(f"\n{current_player.name} has won the game!")

            # Switch to the next player
            current_player_index = (current_player_index + 1) % num_players

        print("\n--- Game Over ---")
        print("Final scores:")
        for player in self.players:
            print(f"{player.name}: {len(player.hand.cards)}")

# Run the game
if __name__ == "__main__":
    rummy_game = RummyGame()
    rummy_game.play()
