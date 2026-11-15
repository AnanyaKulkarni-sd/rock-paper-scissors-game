
import streamlit as st
import random

# Page configuration
st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="✊",
    layout="centered"
)

# Initialize scores
if "wins" not in st.session_state:
    st.session_state.wins = 0

if "losses" not in st.session_state:
    st.session_state.losses = 0

if "draws" not in st.session_state:
    st.session_state.draws = 0

if "result" not in st.session_state:
    st.session_state.result = None

if "computer" not in st.session_state:
    st.session_state.computer = None

if "player" not in st.session_state:
    st.session_state.player = None

# Title
st.title("✊ Rock Paper Scissors ✌️")
st.write("Play against the computer and see who wins!")

st.divider()

# Instructions
st.subheader("How to Play")
st.write("""
- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.
- If both choose the same, it's a Draw!
""")

st.divider()

# Scoreboard
st.subheader("🏆 Scoreboard")

col1, col2, col3 = st.columns(3)

col1.metric("Wins", st.session_state.wins)
col2.metric("Losses", st.session_state.losses)
col3.metric("Draws", st.session_state.draws)

st.divider()

# Player selection
st.subheader("Make Your Choice!")

choices = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}

col1, col2, col3 = st.columns(3)

with col1:
    rock = st.button("✊ Rock", use_container_width=True)

with col2:
    paper = st.button("✋ Paper", use_container_width=True)

with col3:
    scissors = st.button("✌️ Scissors", use_container_width=True)

# Game logic
player_choice = None

if rock:
    player_choice = "Rock"
elif paper:
    player_choice = "Paper"
elif scissors:
    player_choice = "Scissors"

if player_choice:

    computer_choice = random.choice(
        ["Rock", "Paper", "Scissors"]
    )

    st.session_state.player = player_choice
    st.session_state.computer = computer_choice

    # Decide winner
    if player_choice == computer_choice:

        st.session_state.result = "Draw!"
        st.session_state.draws += 1

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or
        (player_choice == "Paper" and computer_choice == "Rock")
        or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):

        st.session_state.result = "You Win! 🎉"
        st.session_state.wins += 1

    else:

        st.session_state.result = "Computer Wins! 🤖"
        st.session_state.losses += 1

# Display result
if st.session_state.result:

    st.divider()
    st.subheader("🎮 Game Result")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Your Choice")
        st.title(
            choices[st.session_state.player]
        )
        st.write(st.session_state.player)

    with col2:
        st.write("Computer's Choice")
        st.title(
            choices[st.session_state.computer]
        )
        st.write(st.session_state.computer)

    if st.session_state.result == "You Win! 🎉":
        st.success(st.session_state.result)

    elif st.session_state.result == "Draw!":
        st.info(st.session_state.result)

    else:
        st.error(st.session_state.result)

# Reset game
st.divider()

if st.button("🔄 Reset Score", use_container_width=True):

    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.draws = 0
    st.session_state.result = None
    st.session_state.player = None
    st.session_state.computer = None

    st.rerun()

st.caption("Made with Python and Streamlit ")
