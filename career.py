from season import simulate_season


def start_career(player):

    print(f"🚀 Career Started: {player.name}")

    while player.age < 38:

        print("\n====================")
        print(f"Age: {player.age}")
        print(f"Club: {player.club}")
        print(f"Overall: {player.rating}")
        print("====================")

        simulate_season(player)

        player.age += 1


    print("\n🏁 Career Finished!")
    print(f"{player.name} has retired at age {player.age}")
