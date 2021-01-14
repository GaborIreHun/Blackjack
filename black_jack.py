
"""

Module Title: Intro to Programming for Data Analytics.
Assignment Type: Individual Practical Assignment.
Project Title: Blackjack Card Game.

"""


################################--Legacy code by Amilcar starts--####################################################

import random

# card class created below to determinate the suit and the rank of the cards what also creates the value of the cards and allow us to call these

class Card():
    def __init__(self, suit, rank, available = True):
        self.suit = suit
        self.rank = rank
        self.available = available

    def __str__(self):
        return "[ " + self.suit + " / " + self.rank + " ]"
        
    def get_value(self):
        if (self.rank == "2" or self.rank == "3" or
            self.rank == "4" or self.rank == "5" or
            self.rank == "6" or self.rank == "7" or
            self.rank == "8" or self.rank == "9" or
            self.rank == "10"):
            val = int(self.rank)
        elif (self.rank == "Jack" or self.rank == "Queen" or
              self.rank == "King"):
            val = 10
        elif (self.rank == "Ace"):
            val = 11
        return val

# deck class created below to determinate the content of same and allow us to call random cards from this deck

class Deck():
    def __init__(self):
        self.cards = []
        suits = ["HEARTS", "CLUBS", "SPADES", "DIAMONS"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
                
    def get_random_card(self):
        while True:
            index = random.randint(0,51)
            if self.cards[index].available:
                self.cards[index].available = False
                return self.cards[index]
    
         
################################^Legacy code ends^####################################################  
      

# player class created below to determinate the players hand and contain the relevant functions
    
class Player():
    def __init__(self):
        self.hand = []     

       
        self.choice = ""
 
    # determination of the printing of the hand
 
    def print_hand(self):
        number_of_cards = len(self.hand)
        
        print()
    
        print()
        for i in range(number_of_cards):
            card = self.hand[i]
            print("[",format(card.suit),"]", "->",format(card.rank),"  ", end="")
  
        print()

        
         
########## credit to tokyoedtech @ https://pastebin.com/WvmEtZDg ##########

# below function calculates the total of the hands

    def calculate_hand(self):
        value = 0
        for card in self.hand:
            value += card.get_value()
 
        return value
 
# below function prints the header

def print_header():
    print("\n\t\t*******Welcome at my BlackJack table!!********")
    
 
# players are created below

dealer = Player()
player1 = Player()
 
# deck is created for the game

deck = Deck()
 
# below function resets hands and deck at each new start

def reset_game():
        
        deck = Deck()
 
        player1.hand.clear()
        player1.choice = ""
 
        dealer.hand.clear()
        dealer.choice = ""

######################### credited script ends ###########################
         

        # below script initiates the first set of deals
 
        player1.hand.append(deck.get_random_card())
         
        dealer.hand.append(deck.get_random_card())
         
        player1.hand.append(deck.get_random_card())
                
        dealer.hand.append(deck.get_random_card())
        
        
# below function terminates program at will when decision is made 
    
def quitter():
    raise SystemExit()
 
# below function is made for the process of the decision making    
 
def decision():
    play_again = input("Would you like to play again? Y)es or N)o?")
    if play_again == "y":
        reset_game()
         
        
    elif play_again == "n":
        print("\n --------------Alright so! See ya again!!--------------")
        quitter()
        
    else:
        print("Try again!")
        decision()
    
# below function initiates, when game progresses to the dealers turn

def dealers_turn():
             
    while(dealer.choice != "S"):
        
        # determination of player's bust and relevant actions 
        
        if(player1.calculate_hand() > 21):
            dealer.choice = "S"
            print_game()
            print("\nYOU BUST")
            print("\n\t***DEALER WINS!***")
            decision()
            
        # determination of dealer's blackjack and relevant actions 
            
        elif(dealer.calculate_hand() == 21):
            print_game()
            print("\n\t***THE DEALER BLACKJACK!!DEALER WINS!***")
            decision()
        
        # determination of dealer's action when dealer has smaller hand
        
        elif(dealer.calculate_hand() < player1.calculate_hand() and dealer.calculate_hand() < 17):
            dealer.hand.append(deck.get_random_card())
            dealer.choice = "H"
            
        # determination of dealer's actions when dealer has less than 17 in hand 
            
        elif (dealer.calculate_hand() < 17):
            dealer.hand.append(deck.get_random_card())
            dealer.choice = "H"
            
        # determination of dealer's actions when dealer has more/or 17 in hand and has more in hand than player
            
        elif(dealer.calculate_hand() > player1.calculate_hand() and dealer.calculate_hand() >= 17):
            dealer.choice = "S"
            print_game()
            
        # determination of dealer's actions when dealer has smaller hand but has more/or 17 in hand 
            
        elif(dealer.calculate_hand() < player1.calculate_hand() and dealer.calculate_hand() >= 17):
            dealer.choice = "S"
            print_game()
            
        # determination of dealer's bust and relevant actions 
                
        elif(dealer.calculate_hand() > 21):
            print_game()
            print("\nDEALER BUSTS")
            print("\n\t***YOU WIN!***")
            decision()
 
            
        else:
            dealer.choice = "S"

# this function is for the actual player, what initiates after the first deal            
            
def player_turn():
    
    while True:
 
 
        while(player1.choice != "S"):
            print_game()
     
            # creating input for the choise of hit or stay
            
            player1.choice = input("\nWould you like to H)it or S)tay? > ").upper()
     
            # determination of dealer's blackjack and relevant actions   
     
            if(dealer.calculate_hand() == 21):
            
                print_game()
                print("\n\t***THE DEALER BLACKJACK!!DEALER WINS!***")
                decision()
                
                
            # determination of player's hit and relevant actions 
     
            elif(player1.choice == "H"):
                player1.hand.append(deck.get_random_card())
     
            print_game()
            
     
            # determination of player's bust and relevant actions 
                
            if(player1.calculate_hand() > 21):
                dealer.choice = "S"
                                
                print_game()
                print("\nYOU BUST")
                print("\n\t***DEALER WINS!***")
                decision()
                
            # determination of player's stay and relevant actions 
                
            elif(player1.choice == "S"):
                dealers_turn()
       
        # determination of push and relevant actions  
                        
        if(player1.calculate_hand() == dealer.calculate_hand()):
            
            print_game()
            print("\n\t***IT'S A PUSH!***")
            decision()
          
        # determination of player's win and relevant actions 
        
        elif(player1.calculate_hand() > dealer.calculate_hand()):
            
            print_game()
            print("\n\t***YOU WIN!***")
            decision()
            
        # determination of dealer's bust and relevant actions 
            
        elif(dealer.calculate_hand() > 21):
            print_game()
            print("\nDEALER BUSTS")
            print("\n\t***YOU WIN!***")
            decision()
   
        # determination of player's blackjack and relevant actions 
         
        elif(player1.calculate_hand() == 21):
            print_game()
            print("\n\t***YOU HAVE BLACKJACK!!YOU WIN!***")
            decision()
    
            
        else:
            
            print_game()
            print("\n\t***DEALER WINS!***")
            decision()

# the below function is for the visualization of the game, print header, cards and cards value

def print_game():
            
    print_header()
    
    # printing dealer's cards 
 
    print("\n---DEALER---")
    dealer.print_hand()
    
    # printing the value of the dealer's cards
    
    if(dealer.choice == "S"):
        print("\n\tHand value: {}".format(dealer.calculate_hand()))
    else:
        print()
        
    # printing player's cards
    
    print("\n---YOU---")
    player1.print_hand()
    
    # printing the value of the player's cards
    
    print("\n\tHand value: {}".format(player1.calculate_hand()))

# the game is initiated below by resetting palyers and initiating the player function
    
reset_game()

player_turn()
 
