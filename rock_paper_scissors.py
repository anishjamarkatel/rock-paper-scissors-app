import streamlit as st
import random

st.title("✊ Rock 🧻 Paper ✂️ Scissors")

choices = ["rock", "paper", "scissors"]
user_choice = st.radio("Choose one:", choices, horizontal=True)
computer_choice = random.choice(choices)

if st.button("Play"):
    st.write(f"🤖 Computer chose: **{computer_choice}**")

    if user_choice == computer_choice:
        st.info("It's a draw!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        st.success("🎉 You won!")
    else:
        st.error("😢 You lose!")
