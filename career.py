import random


class Career:

    def __init__(self, player):

        self.player = player

        self.season = 1

        self.club_history = [
            player.club
        ]

        self.trophies = []

        self.awards = []

        self.money = 0



    def start_season(self):

        return (
            f"Season {self.season} begins at "
            f"{self.player.club}!"
        )



    def end_season(self):

        self.player.age_up()

        self.season += 1



    def train(self):

        upgrades = [

            "pace",
            "shooting",
            "passing",
            "dribbling",
            "physical"

        ]

        chosen = random.choice(upgrades)

        self.player.upgrade(chosen)

        return (
            f"Training complete! "
            f"{chosen.capitalize()} improved."
        )



    def transfer_offer(self):

        clubs = [

            "Manchester United",
            "Real Madrid",
            "Barcelona",
            "Manchester City",
            "Bayern Munich",
            "PSG",
            "Liverpool",
            "Inter Milan"

        ]


        if random.randint(1,100) <= 30:

            new_club = random.choice(clubs)


            self.player.transfer(
                new_club
            )


            self.club_history.append(
                new_club
            )


            return (
                f"🚨 Transfer completed! "
                f"You joined {new_club}"
            )


        return (
            "No transfer offers this season."
        )



    def check_trophies(self):

        chance = random.randint(1,100)


        if chance <= 25:

            trophy = random.choice(

                [
                    "League Title",
                    "Champions League",
                    "Domestic Cup"
                ]

            )


            self.trophies.append(
                trophy
            )


            return (
                f"🏆 You won the {trophy}!"
            )


        return "No trophies this season."



    def check_awards(self):

        awards = []


        if self.player.goals >= 30:

            self.awards.append(
                "Golden Boot"
            )

            awards.append(
                "Golden Boot"
            )


        if self.player.rating >= 90:

            self.awards.append(
                "Ballon d'Or"
            )

            awards.append(
                "Ballon d'Or"
            )


        if len(awards) > 0:

            return (
                "🌟 Awards won: "
                + ", ".join(awards)
            )


        return "No major awards."



    def summary(self):

        return {

            "Season": self.season,

            "Club History":
                self.club_history,

            "Trophies":
                self.trophies,

            "Awards":
                self.awards,

            "Career Goals":
                self.player.goals,

            "Career Assists":
                self.player.assists

        }
