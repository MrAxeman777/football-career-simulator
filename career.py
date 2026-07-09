from season import simulate_season
from transfer import transfer_window
from trophies import check_trophies
from national_team import national_team_callup


def start_career(player):

    print(f"🚀 Career Started: {player.name}")

    while player.age < 38:

        print("\n====================")
        print(f"Age: {player.age}")
        print(f"Club: {player.club}")
        print(f"Overall: {player.rating}")
        print("====================")

        # Club season
        simulate_season(player)

        # Trophy chances
        check_trophies(player)

        # International football
        national_team_callup(player)

        # Transfers every summer
        transfer_window(player)

        # Age increases
        player.age += 1


    print("\n🏁 Career Finished!")
    print(f"{player.name} retired at age {player.age}")
