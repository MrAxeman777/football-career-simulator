class Awards:

    def __init__(self):

        self.awards = []


    def add_award(self, award):

        if award not in self.awards:

            self.awards.append(award)


    def get_awards(self):

        return self.awards
