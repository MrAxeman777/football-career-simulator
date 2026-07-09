import streamlit as st
import random

from player import Player
from career import Career
from trophies import TrophyRoom
from awards import Awards


st.set_page_config(
    page_title="Football Career Simulator",
    page_icon="⚽"
)


st.title("⚽ Football Career Simulator")


name = st.text_input(
    "Player Name"
)


position = st.selectbox(
    "Position",
    [
        "ST",
        "LW",
        "RW",
        "CAM",
        "CM",
        "CDM",
        "CB",
        "LB",
        "RB",
        "GK"
    ]
)


nationality = st.text_input(
    "Nationality"
)


seasons = st.slider(
    "Career Length",
    1,
    25,
    10
)


if st.button("🚀 Start Career"):


    player = Player(
        name,
        position,
        nationality
    )


    career = Career(player)

    trophies = TrophyRoom()

    awards = Awards()


    st.header("Career Begins!")

    clubs = [

        "Manchester United",
        "Real Madrid",
        "Barcelona",
        "Manchester City",
        "Bayern Munich",
        "PSG",
        "Liverpool"

    ]


    current_club = random.choice(clubs)


    for season in range(1, seasons + 1):

        goals = random.randint(5,45)

        assists = random.randint(2,25)


        player.add_stats(
            goals,
            assists
        )


        improvement = random.randint(1,4)

        player.improve(
            improvement
        )


        won = []


        if random.randint(1,100) <= 35:

            trophy = random.choice(
                [
                    "League Title",
                    "Champions League",
                    "Domestic Cup"
                ]
            )

            trophies.add_trophy(trophy)

            won.append(trophy)


        if goals >= 35:

            awards.add_award(
                "Golden Boot"
            )


        if player.rating >= 90:

            awards.add_award(
                "Ballon d'Or"
            )


        career.add_season(

            season,
            current_club,
            goals,
            assists,
            won

        )


        st.subheader(
            f"Season {season} - {current_club}"
        )

        st.write(
            f"⚽ Goals: {goals}"
        )

        st.write(
            f"🎯 Assists: {assists}"
        )

        st.write(
            f"⭐ Rating: {player.rating}"
        )


    st.success(
        "Career Finished!"
    )


    st.header("🏆 Final Player")

    st.write(player.__dict__)


    st.header("🏆 Trophies")

    st.write(
        trophies.get_trophies()
    )


    st.header("🌟 Awards")

    st.write(
        awards.get_awards()
    )


    st.header("📜 Career History")

    st.write(
        career.get_history()
    )
