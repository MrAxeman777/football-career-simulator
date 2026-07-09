import random


clubs = [
    "Manchester United",
    "Real Madrid",
    "Barcelona",
    "Bayern Munich",
    "Arsenal",
    "Chelsea",
    "Paris Saint-Germain"
]


def transfer_window(player):

    print("\n🔄 Transfer Window Open!")

    if player.rating >= 75:

        offer = random.choice(clubs)

        print(f"\n{offer} is interested in {player.name}!")

        decision = input(
            "Accept transfer? (yes/no): "
        )

        if decision.lower() == "yes":

            player.club = offer
            player.clubs.append(offer)

            print(
                f"\n✅ {player.name} transferred to {offer}!"
            )

        else:
            print(
                f"\n{player.name} stayed at {player.club}."
            )

    else:
        print("No major clubs are interested yet.")
