from card import Card
from deck import Deck

"""
    Evaluate the DeckOfCards.
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def sayHello(self):
        print("Hi! My name is {}".format(self.name))
        return self

    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    def showHand(self):
        print("{}'s hand: {}".format(self.name, self.hand))
        return self

    def discard(self):
        return self.hand.pop()


if __name__ == "__main__":

    try:

        myDeck = Deck()
        myDeck.shuffle()
        print("\n\t-------  playe names  ---------\n")
        for player in range(4):
            player_name = str(
                input("Enter {}.player name : ".format(player+1)))
            name = Player(player_name)
            name.sayHello()
            name.draw(myDeck, 5)
            name.showHand()

    except ValueError:

        print("Error")
