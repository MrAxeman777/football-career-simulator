import streamlit as st

from player import Player
from career import start_career


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

    player.show_profile()
