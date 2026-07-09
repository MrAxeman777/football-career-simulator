import random


def national_team_callup(player):

    print("\n🇺🇸 National Team Check...")

    if player.rating >= 75:

        print(f"\n🔥 {player.name} has been called up to the USA National Team!")

        games = random.randint(3, 15)
        goals = random.randint(0, 8)
        assists = random.randint(0, 6)

        player.international_games += games
        player.international_goals += goals
        player.international_assists += assists

        print(f"""
International Season:

Games: {games}
Goals: {goals}
Assists: {assists}
""")

    else:
        print("Not selected for the national team yet.")
