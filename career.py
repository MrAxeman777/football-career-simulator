from season import simulate_season
from transfer import transfer_window
from trophies import check_trophies


def start_career(player):

    print(f"🚀 Career Started: {player.name}")

    while player.age < 38:

        print("\n====================")
        print(f"Age: {player.age}")
        print(f"Club: {player.club}")
        print(f"Overall: {player.rating}")
        print("====================")

        simulate_season(player)

        # Trophy check after each season
        check_trophies(player)

        # Transfer window every summer
        transfer_window(player)

        # Player gets older
        player.age += 1


    print("\n🏁 Career Finished!")
    print(f"{player.name} retired at age {player.age}")
