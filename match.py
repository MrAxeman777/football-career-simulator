import random


def play_match(player):

    goals = 0
    assists = 0


    performance = (

        player.rating
        + player.dribbling
        + player.shooting

    ) / 3


    chance = random.randint(1,100)


    if chance < performance:

        goals = random.randint(0,3)

        assists = random.randint(0,2)

    else:

        goals = random.randint(0,1)

        assists = 0



    player.add_match_stats(
        goals,
        assists
    )


    rating = random.randint(
        5,
        10
    )


    return {

        "goals": goals,
        "assists": assists,
        "match_rating": rating

    }
