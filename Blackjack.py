import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

player = [random.choice(cards), random.choice(cards)]
dealer = [random.choice(cards), random.choice(cards)]

while True:
    print("\nYour cards:", player)
    print("Total:", sum(player))

    if sum(player) > 21:
        print("Bust! You lose.")
        break

    choice = input("Do you want to draw a card? (y/n): ")

    if choice.lower() == "y":
        player.append(random.choice(cards))
    else:
        break

while sum(dealer) < 17:
    dealer.append(random.choice(cards))

player_total = sum(player)
dealer_total = sum(dealer)

print("\nDealer's cards:", dealer, "Total:", dealer_total)

if dealer_total > 21:
    print("Dealer busts! You win.")
elif player_total > dealer_total:
    print("You win!")
elif player_total < dealer_total:
    print("You lose!")
else:
    print("It's a tie!")
