import random


def simulate_season(player):

    print("\n--- Season Started ---")

    games = random.randint(20, 45)
    goals = random.randint(5, 25)
    assists = random.randint(5, 20)

    player.games += games
    player.goals += goals
    player.assists += assists


    # Player growth
    growth = random.randint(1, 4)

    if player.rating < player.potential:
        player.rating += growth

        if player.rating > player.potential:
            player.rating = player.potential


    # Awards
    if goals + assists >= 25:
        player.awards.append("Breakthrough Player Award")

    print(f"""
Season Finished!

Games: {games}
Goals: {goals}
Assists: {assists}

New Rating: {player.rating}
""")
