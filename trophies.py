import random


def check_trophies(player):

    chance = random.randint(1, 100)

    if chance <= 25:
        trophy = "League Title 🏆"
        player.trophies.append(trophy)
        print(f"\n🏆 Won: {trophy}")

    if player.rating >= 85 and chance <= 15:
        trophy = "Champions League 🏆"
        player.trophies.append(trophy)
        print(f"\n🏆 Won: {trophy}")

    if player.age >= 18 and chance <= 10:
        trophy = "International Trophy 🌎"
        player.trophies.append(trophy)
        print(f"\n🏆 Won: {trophy}")
