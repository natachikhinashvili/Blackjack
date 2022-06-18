from values import values
class Card:
  def __init__(self,rank,suit):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]
  
  def __str__(self):
    return self.rank + ' of ' + self.suit
