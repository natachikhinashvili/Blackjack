from Deck import Deck
from chips import Chips
from hand import Hand

carddeck = Deck().shuffle()
hand = Hand()
chips = Chips()

def add(i):
  hand.add_card(carddeck[i])
  hand.add_card_dealer(carddeck[len(carddeck) - i - 1])
  carddeck.pop(i)
  carddeck.pop(len(carddeck) - i - 1)

for _ in range(2):
  add(_)
bet = int(input('input your bet :'))
if bet > chips.total:
  print('out of bounds')
 
print(f'one of dealers cards {hand.dealercards[0]}')
playing = True
  
while playing:
  def hit_or_stand(hand):
    print(f'your cards: hand.cards {hand.cards}')
    print(f'one of dealers card : {hand.dealercards[0]}')
    global playing
    answer = input('Hit or Stand? (h or s):' )

    if answer == 'h':
      playing = True
      for _ in range(1):
        add(_)
    elif answer == 's':
      playing = False

  hit_or_stand(hand)
 
  if hand.value > 21:
    chips.lose_bet(bet)
    print('Busted! You lose!')
    print(hand.dealercards)
    break

  if hand.dealervalue >= 17:
    chips.win_bet(bet)
    print('You win!')
    print(f'dealers cards: {hand.dealercards}')
    print(f'your remaining chips : {chips.total}')
    break;

answer = input('Would you like to play again? (y or n) : ')
if answer == 'y':
  playing = True
elif answer == 'n':
  playing = False