# The code for Coin Toss

import random
coin=["Heads","Tails"]
Toss=random.choice(coin)
Selection= input("Heads or Tails:")
if Selection==Toss:
    print("You Win! The coin landed on " + Toss)
else:
    print("You lose! The coin landed on " + Toss)
