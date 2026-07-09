class Player:

    def __init__(self, name, position, nationality):

        self.name = name
        self.position = position
        self.nationality = nationality

        self.age = 16
        self.rating = 65

        self.goals = 0
        self.assists = 0


    def improve(self, amount):

        self.rating += amount

        if self.rating > 99:
            self.rating = 99


    def add_stats(self, goals, assists):

        self.goals += goals
        self.assists += assists


    def __str__(self):

        return (
            f"Name: {self.name}\n"
            f"Position: {self.position}\n"
            f"Nationality: {self.nationality}\n"
            f"Age: {self.age}\n"
            f"Rating: {self.rating}\n"
            f"Career Goals: {self.goals}\n"
            f"Career Assists: {self.assists}"
        )
