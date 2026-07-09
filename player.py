class Player:
    def __init__(self, name, position, age, nationality, club, rating, potential):
        # Basic information
        self.name = name
        self.position = position
        self.age = age
        self.nationality = nationality
        self.club = club

        # Ratings
        self.rating = rating
        self.potential = potential

        # Player attributes
        self.pace = 78
        self.shooting = 81
        self.passing = 87
        self.dribbling = 83
        self.defending = 58
        self.physical = 73

        # Club career stats
        self.games = 0
        self.goals = 0
        self.assists = 0

        # International stats
        self.international_games = 0
        self.international_goals = 0
        self.international_assists = 0

        # Achievements
        self.trophies = []
        self.awards = []

        # Career history
        self.clubs = [club]


    def show_profile(self):
        print("-------------------------")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Age: {self.age}")
        print(f"Nationality: {self.nationality}")
        print(f"Club: {self.club}")

        print("\nRating:")
        print(f"Overall: {self.rating}")
        print(f"Potential: {self.potential}")

        print("\nAttributes:")
        print(f"Pace: {self.pace}")
        print(f"Shooting: {self.shooting}")
        print(f"Passing: {self.passing}")
        print(f"Dribbling: {self.dribbling}")
        print(f"Defending: {self.defending}")
        print(f"Physical: {self.physical}")

        print("\nClub Career:")
        print(f"Games: {self.games}")
        print(f"Goals: {self.goals}")
        print(f"Assists: {self.assists}")

        print("\nInternational Career:")
        print(f"Games: {self.international_games}")
        print(f"Goals: {self.international_goals}")
        print(f"Assists: {self.international_assists}")

        print("\nTrophies:")
        for trophy in self.trophies:
            print(f"🏆 {trophy}")

        print("\nAwards:")
        for award in self.awards:
            print(f"⭐ {award}")

        print("-------------------------")
