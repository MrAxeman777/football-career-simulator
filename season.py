from match import play_match


def simulate_season(player):

    print("\n--- Season Started ---")

    total_games = 30
    total_rating = 0


    for game in range(total_games):

        print(f"\nMatch {game + 1}/{total_games}")

        rating = play_match(player)

        total_rating += rating


    average_rating = round(total_rating / total_games, 2)


    print(f"""
====================
Season Finished!

Games: {player.games}
Goals: {player.goals}
Assists: {player.assists}

Average Match Rating:
{average_rating}

Overall:
{player.rating}
====================
""")


    # Player growth
    if average_rating >= 8:
        player.rating += 3

    elif average_rating >= 7:
        player.rating += 2

    else:
        player.rating += 1


    if player.rating > player.potential:
        player.rating = player.potential
