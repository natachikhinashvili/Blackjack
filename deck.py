from card import Card
from values import ranks
from values import suits

import random

class Deck:

  def __init__(self):
    self.all_cards = []
    self.cardval = 0
    for suit in suits:
      for rank in ranks:
        self.all_cards.append(Card(rank,suit).__str__())

  def shuffle(self):
    random.shuffle(self.all_cards)
    return self.all_cards