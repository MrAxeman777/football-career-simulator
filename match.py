import random


opponents = [
    "LA Galaxy",
    "Inter Miami",
    "Seattle Sounders",
    "New York City FC",
    "Atlanta United",
    "Sporting KC"
]


def play_match(player):

    opponent = random.choice(opponents)

    print("\n====================")
    print(f"⚽ {player.club} vs {opponent}")
    print("====================")


    goals = 0
    assists = 0

    chances = random.randint(1, 5)


    for i in range(chances):

        event = random.randint(1, 100)

        if event <= 35:

            goals += 1

            minute = random.randint(1, 90)

            print(
                f"{minute}' GOAL!!! {player.name} scores!"
            )

        elif event <= 60:

            assists += 1

            minute = random.randint(1, 90)

            print(
                f"{minute}' ASSIST!!! {player.name} creates a goal!"
            )


    rating = round(random.uniform(6.5, 10.0), 1)


    player.goals += goals
    player.assists += assists
    player.games += 1


    print(f"""
Full Time!

{player.name} Match Stats:

Goals: {goals}
Assists: {assists}
Match Rating: {rating}
""")

    return rating
