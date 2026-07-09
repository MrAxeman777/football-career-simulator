import streamlit as st

from player import Player
from career import Career
from match import play_match
from events import random_event


st.set_page_config(
    page_title="⚽ Soccer Career Mode",
    page_icon="⚽"
)


st.title("⚽ Soccer Career Mode")
st.caption("Retro Bowl style football career simulator")


# Create player
if "career" not in st.session_state:

    st.session_state.career = None



if st.session_state.career is None:


    st.header("Create Your Player")


    name = st.text_input(
        "Player Name"
    )


    nationality = st.text_input(
        "Nationality"
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


    if st.button("🚀 Start Career"):


        player = Player(

            name,
            position,
            nationality

        )


        career = Career(
            player
        )


        st.session_state.career = career


        st.rerun()



else:


    career = st.session_state.career

    player = career.player



    st.header(
        f"{player.name} - {player.club}"
    )


    # Player card

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Overall",
            player.rating
        )


    with col2:

        st.metric(
            "Age",
            player.age
        )


    with col3:

        st.metric(
            "Goals",
            player.goals
        )



    st.divider()


    # Actions


    st.subheader(
        "Actions"
    )


    if st.button("⚽ Play Match"):


        result = play_match(
            player
        )


        st.success(
            "Match Complete!"
        )


        st.write(
            f"Goals: {result['goals']}"
        )


        st.write(
            f"Assists: {result['assists']}"
        )


        st.write(
            f"Match Rating: {result['match_rating']}/10"
        )


        st.info(
            random_event(player)
        )




    if st.button("🏋 Train"):


        message = career.train()


        st.success(
            message
        )




    if st.button("🔄 Transfer Window"):


        st.info(
            career.transfer_offer()
        )




    if st.button("⏭ End Season"):


        st.write(
            career.check_trophies()
        )


        st.write(
            career.check_awards()
        )


        career.end_season()


        st.success(
            f"Season {career.season} started!"
        )




    st.divider()


    st.subheader(
        "📊 Player Stats"
    )


    st.json(
        player.info()
    )



    st.subheader(
        "🏆 Career Summary"
    )


    st.json(
        career.summary()
    )
