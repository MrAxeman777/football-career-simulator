from player import Player
from career import start_career


ashwin = Player(
    "Ashwin",
    "LW",
    17,
    "USA",
    "FC Dallas Academy",
    72,
    93
)


ashwin.trophies.append("U19 League Winner")
ashwin.awards.append("Young Player of the Year")


ashwin.show_profile()


start_career(ashwin)


ashwin.show_profile()
