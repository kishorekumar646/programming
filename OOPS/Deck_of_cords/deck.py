from card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def show(self):
        for card in self.cards:
            print(card.show())

    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]

    def deal(self):
        return self.cards.pop()
