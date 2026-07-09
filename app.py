import random
import time

from player import Player
from career import Career
from trophies import TrophyRoom
from awards import Awards


def main():

    print("====================================")
    print("⚽ FOOTBALL CAREER MODE SIMULATOR ⚽")
    print("====================================")

    # Create player
    name = input("Enter your player's name: ")

    position = input(
        "Choose position (ST, LW, RW, CAM, CM, CDM, CB, LB, RB, GK): "
    ).upper()

    nationality = input("Enter nationality: ")

    player = Player(
        name,
        position,
        nationality
    )

    career = Career(player)
    trophies = TrophyRoom()
    awards = Awards()


    print("\nCareer Started!")
    print("------------------------------------")

    print(player)


    seasons = int(input("\nHow many seasons do you want to simulate? "))


    for year in range(1, seasons + 1):

        print("\n==============================")
        print(f"Season {year}")
        print("==============================")

        time.sleep(1)


        # Generate season stats
        goals = random.randint(0, 35)
        assists = random.randint(0, 20)
        matches = random.randint(20, 55)

        trophies_won = []


        print("\nSeason Stats:")
        print(f"Matches: {matches}")
        print(f"Goals: {goals}")
        print(f"Assists: {assists}")


        # Player growth
        improvement = random.randint(1, 4)

        player.rating += improvement

        if player.rating > 99:
            player.rating = 99


        print(
            f"\n⭐ Overall increased by {improvement}!"
        )
        print(
            f"New Rating: {player.rating}"
        )


        # Awards
        if goals >= 30:

            awards.add_award(
                "Golden Boot"
            )

            print(
                "🏆 You won the Golden Boot!"
            )


        if player.rating >= 90:

            awards.add_award(
                "Ballon d'Or"
            )

            print(
                "🌟 You won the Ballon d'Or!"
            )


        # Trophies
        chance = random.randint(1, 100)

        if chance <= 30:

            trophy = random.choice(
                [
                    "League Title",
                    "Champions League",
                    "Domestic Cup"
                ]
            )

            trophies.add_trophy(
                trophy
            )

            trophies_won.append(trophy)

            print(
                f"🏆 Won {trophy}!"
            )


        # Save season
        career.add_season(
            year,
            goals,
            assists,
            trophies_won
        )


        # Transfer chance

        if random.randint(1,100) <= 25:

            new_club = random.choice(
                [
                    "Manchester United",
                    "Real Madrid",
                    "Barcelona",
                    "Bayern Munich",
                    "PSG",
                    "Manchester City",
                    "Liverpool"
                ]
            )

            career.transfer(
                new_club
            )

            print(
                f"🔄 Transferred to {new_club}"
            )


    print("\n\n====================================")
    print("🏁 CAREER COMPLETE")
    print("====================================")


    print("\nPLAYER PROFILE")
    print("------------------------------------")
    print(player)


    print("\nTROPHIES")
    print("------------------------------------")

    trophies.show()


    print("\nAWARDS")
    print("------------------------------------")

    awards.show()


    print("\nCAREER HISTORY")
    print("------------------------------------")

    career.show_history()



if __name__ == "__main__":
    main()
