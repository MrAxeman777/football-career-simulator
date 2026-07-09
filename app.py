import streamlit as st

from player import Player
from season import simulate_season
from transfer import transfer_window
from trophies import check_trophies
from awards import check_awards
from national_team import national_team_callup


st.set_page_config(
    page_title="Football Career Simulator",
    page_icon="⚽"
)


st.title("⚽ Football Career Simulator")

st.write(
    "Create your player and simulate an entire football career!"
)


# Player creation

name = st.text_input(
    "Player Name",
    "Ashwin"
)


position = st.selectbox(
    "Position",
    ["LW", "RW", "ST", "CAM", "CM"]
)


age = st.number_input(
    "Age",
    15,
    40,
    17
)


nationality = st.text_input(
    "Nationality",
    "USA"
)


club = st.text_input(
    "Starting Club",
    "FC Dallas Academy"
)


rating = st.slider(
    "Starting Rating",
    50,
    99,
    72
)


potential = st.slider(
    "Potential",
    50,
    99,
    93
)



if st.button("🚀 Start Career"):

    player = Player(
        name,
        position,
        age,
        nationality,
        club,
        rating,
        potential
    )


    st.success(
        f"{player.name}'s career has started!"
    )


    # Career simulation

    seasons = []

    while player.age < 38:

        current_age = player.age

        simulate_season(player)

        check_trophies(player)

        check_awards(player)

        national_team_callup(player)

        transfer_window(player)


        seasons.append(
            {
                "Age": current_age,
                "Club": player.club,
                "Rating": player.rating,
                "Goals": player.goals,
                "Assists": player.assists
            }
        )


        player.age += 1



    # Results page

    st.header("👤 Final Player Card")


    col1, col2 = st.columns(2)


    with col1:
        st.write(
            f"""
            **Name:** {player.name}

            **Position:** {player.position}

            **Nationality:** {player.nationality}

            **Final Club:** {player.club}

            **Final Rating:** {player.rating}

            **Potential:** {player.potential}
            """
        )


    with col2:

        st.write(
            f"""
            **Games:** {player.games}

            **Goals:** {player.goals}

            **Assists:** {player.assists}

            **International Games:** {player.international_games}

            **International Goals:** {player.international_goals}
            """
        )


    st.header("🏆 Trophies")

    if player.trophies:

        for trophy in player.trophies:
            st.write("🏆", trophy)

    else:
        st.write("No trophies won")



    st.header("⭐ Awards")

    if player.awards:

        for award in player.awards:
            st.write("⭐", award)

    else:
        st.write("No awards won")



    st.header("📈 Career Timeline")

    st.dataframe(
        seasons
    )
