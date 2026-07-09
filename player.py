class Player:

    def __init__(self, name, position, nationality):

        self.name = name
        self.position = position
        self.nationality = nationality

        # Career info
        self.age = 17
        self.club = "Youth Academy"

        # Overall
        self.rating = 60

        # Skills
        self.pace = 60
        self.shooting = 60
        self.passing = 60
        self.dribbling = 60
        self.defending = 60
        self.physical = 60

        # Career stats
        self.matches = 0
        self.goals = 0
        self.assists = 0

        self.fame = 0
        self.salary = 0



    def upgrade(self, attribute):

        if hasattr(self, attribute):

            value = getattr(self, attribute)

            if value < 99:

                setattr(
                    self,
                    attribute,
                    min(value + 3, 99)
                )

                self.update_rating()



    def update_rating(self):

        skills = [

            self.pace,
            self.shooting,
            self.passing,
            self.dribbling,
            self.defending,
            self.physical

        ]

        self.rating = sum(skills) // len(skills)



    def add_match_stats(self, goals, assists):

        self.matches += 1
        self.goals += goals
        self.assists += assists



    def age_up(self):

        self.age += 1



    def transfer(self, club):

        self.club = club



    def info(self):

        return {

            "Name": self.name,
            "Nationality": self.nationality,
            "Position": self.position,
            "Club": self.club,

            "Age": self.age,
            "Overall": self.rating,

            "Pace": self.pace,
            "Shooting": self.shooting,
            "Passing": self.passing,
            "Dribbling": self.dribbling,
            "Defending": self.defending,
            "Physical": self.physical,

            "Matches": self.matches,
            "Goals": self.goals,
            "Assists": self.assists

        }
