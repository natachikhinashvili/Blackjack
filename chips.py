class Chips:
    
    def __init__(self):
        self.total = 100 
        
    def win_bet(self,bet):
       self.total += bet
    
    def lose_bet(self,bet):
      self.total -= bet