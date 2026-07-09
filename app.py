import streamlit as st

from player import Player
from season import simulate_season


st.title("⚽ Football Career Simulator")

st.write("Create your player and start your legendary career!")


name = st.text_input("Player Name", "Ashwin")

position = st.selectbox(
    "Position",
    ["LW", "RW", "ST", "CAM", "CM"]
)

age = st.number_input(
    "Age",
    min_value=15,
    max_value=40,
    value=17
)

nationality = st.text_input(
    "Nationality",
    "USA"
)

club = st.text_input(
    "Starting Club",
    "FC Dallas Academy"
)


if st.button("Start Career"):

    player = Player(
        name,
        position,
        age,
        nationality,
        club,
        72,
        93
    )


    st.success(
        f"{name}'s career has started!"
    )


    st.header("👤 Player Profile")

    st.write(f"**Name:** {player.name}")
    st.write(f"**Position:** {player.position}")
    st.write(f"**Club:** {player.club}")
    st.write(f"**Overall:** {player.rating}")
    st.write(f"**Potential:** {player.potential}")


    st.header("📊 Season Simulation")

    simulate_season(player)


    st.write(f"Games: {player.games}")
    st.write(f"Goals: {player.goals}")
    st.write(f"Assists: {player.assists}")
    st.write(f"New Rating: {player.rating}")
