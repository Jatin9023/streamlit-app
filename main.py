import streamlit as st
import random

st.title("🎯 Guess The Number Game")

# Number generate sirf ek baar ho
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.guesses = 0

guess = st.number_input(
    "Guess a number between 1 and 100",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("Check"):
    st.session_state.guesses += 1

    if guess < st.session_state.number:
        st.warning("🔼 Higher number please")
    elif guess > st.session_state.number:
        st.warning("🔽 Lower number please")
    else:
        st.success(
            f"🎉 Correct! Number was {st.session_state.number} "
            f"in {st.session_state.guesses} attempts"
        )

        # Game reset
        st.session_state.number = random.randint(1, 100)
        st.session_state.guesses = 0

