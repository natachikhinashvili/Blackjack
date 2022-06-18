from values import values

class Hand:
    def __init__(self):
      self.cards = []
      self.dealercards = []
      self.value = 0   
      self.dealervalue = 0
    
    def add_card(self,card):
      self.cards.append(card)
      self.value += values[card.split(' ')[0]]
      
    def add_card_dealer(self,card):
      self.dealercards.append(card)
      self.dealervalue += values[card.split(' ')[0]]