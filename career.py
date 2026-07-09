from season import simulate_season
from transfer import transfer_window


def start_career(player):

    print(f"🚀 Career Started: {player.name}")

    while player.age < 38:

        print("\n====================")
        print(f"Age: {player.age}")
        print(f"Club: {player.club}")
        print(f"Overall: {player.rating}")
        print("====================")

        simulate_season(player)

        # Transfer window every summer
        transfer_window(player)

        player.age += 1


    print("\n🏁 Career Finished!")
    print(f"{player.name} retired at age {player.age}")
