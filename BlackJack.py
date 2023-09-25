import random
try:
    # Global variables
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    values = {'2': 2, 
              '3': 3, 
              '4': 4, 
              '5': 5, 
              '6': 6, 
              '7': 7, 
              '8': 8, 
              '9': 9, 
              '10': 10, 
              'J': 10, 
              'Q': 10, 
              'K': 10, 
              'A': 11}


    class Card:
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

        def __str__(self):
            return f"{self.rank} of {self.suit}"


    class Deck:
        def __init__(self):
            self.cards = []
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(suit, rank))

        def shuffle(self):
            random.shuffle(self.cards)

        def deal_card(self):
            return self.cards.pop()

            
    class Hand:
        def __init__(self):
            self.cards = []
            self.value = 0
            self.aces = 0

        def add_card(self, card):
            self.cards.append(card)
            self.value += values[card.rank]
            if card.rank == 'A':
                self.aces += 1

        def adjust_for_ace(self):
            while self.value > 21 and self.aces:
                self.value -= 10
                self.aces -= 1


    class Game:
        def __init__(self):
            self.deck = Deck()
            self.deck.shuffle()
            self.player_hand = Hand()
            self.dealer_hand = Hand()

        def start_game(self):
            print("Welcome to Blackjack!")
            self.player_hand.add_card(self.deck.deal_card())
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())
            self.play_game()

        def play_game(self):
            game_over = False

            while not game_over:
                self.display_hands()

                if self.player_hand.value == 21:
                    self.end_game("Blackjack! You win!")
                    break

                action = input("What would you like to do? Hit or Stand? ").lower()

                if action == 'hit':
                    self.player_hand.add_card(self.deck.deal_card())
                    self.player_hand.adjust_for_ace()

                    if self.player_hand.value > 21:
                        self.end_game("Busted! You lose!")
                        break
                elif action == 'stand':
                    while self.dealer_hand.value < 17:
                        self.dealer_hand.add_card(self.deck.deal_card())
                        self.dealer_hand.adjust_for_ace()

                    self.display_hands()

                    if self.dealer_hand.value > 21:
                        self.end_game("Dealer busts! You win!")
                    elif self.dealer_hand.value > self.player_hand.value:
                        self.end_game("Dealer wins!")
                    elif self.dealer_hand.value < self.player_hand.value:
                        self.end_game("You win!")
                    else:
                        self.end_game("It's a tie!")
                        
                    break

        def display_hands(self):
            print("\nPlayer's hand:", ', '.join(str(card) for card in self.player_hand.cards))
            print("Player's hand value:", self.player_hand.value)
            print("\nDealer's hand:", ', '.join(str(card) for card in self.dealer_hand.cards))
            print("Dealer's hand value:", self.dealer_hand.value)

        @staticmethod
        def end_game(message):
            print(message)
            print("\nThanks for playing!")

    # Starting the game
    game = Game()
    game.start_game()
    
except KeyboardInterrupt:
    print("\n\nThanks for playing!")