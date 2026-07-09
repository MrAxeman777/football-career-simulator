import random


def random_event(player):

    events = [

        "A scout from a big club watched you play!",
        "Fans love your performances!",
        "You were named Player of the Match!",
        "Your coach wants you to improve!",
        "A rival challenged you!",
        "You became a team leader!"

    ]


    event = random.choice(events)


    reward = random.randint(0,3)


    player.fame += reward


    return event
