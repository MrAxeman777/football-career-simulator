import random


def check_awards(player):

    print("\n🏅 Award Ceremony...")

    # Young Player Award
    if player.age <= 21 and player.rating >= 80:
        award = "Young Player of the Year ⭐"
        player.awards.append(award)
        print(f"🏆 Won: {award}")


    # Golden Boot
    if player.goals >= 20:
        award = "Golden Boot 🥾"
        player.awards.append(award)
        print(f"🏆 Won: {award}")


    # Player of the Year
    if player.rating >= 90:
        award = "Player of the Year 🌟"
        player.awards.append(award)
        print(f"🏆 Won: {award}")


    # Ballon d'Or chance
    ballon_chance = random.randint(1, 100)

    if player.rating >= 92 and ballon_chance <= 20:
        award = "Ballon d'Or 🥇"
        player.awards.append(award)
        print(f"🏆 Won: {award}")
