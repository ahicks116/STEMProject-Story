import streamlit as st

st.title("🌩️ Choose Your Own Adventure")

st.write("The day started off great—clear skies and a warm breeze. A perfect day for a walk.")
st.write("As you were on your walk, the wind started to pick up and the skies turned grey...")

choice1 = st.text_input("The weather's starting to make you nervous. Do you want to continue walking, or find somewhere to wait out the storm? (continue/wait)").strip().lower()

if choice1 == "wait":
    choice2 = st.text_input("You run over to a nearby shack. Do you want to go in, or wait it out under a nearby tree instead? (shack/tree)").strip().lower()

    if choice2 == "tree":
        st.success("🌳 Good idea! You waited out the storm and can now return home safe.")
        choice3 = st.text_input("As you're walking home, you see something shiny in the grass. What do you do? (pick it up/ignore)").strip().lower()

        if choice3 == "pick it up":
            st.success("💎 It's a magical coin that brings you luck forever. You live a happy life. The end!")
            if st.button("Restart"):
                st.experimental_rerun()
        elif choice3 == "ignore":
            st.write("You leave it alone and walk home safely. Life goes on. The end.")
            if st.button("Restart"):
                st.experimental_rerun()
        elif choice3 != "":
            st.write("That wasn't an option. Your story ends here.")
            if st.button("Restart"):
                st.experimental_rerun()

    elif choice2 == "shack":
        st.write("🧙‍♀️ Bad choice! You opened the door and were trapped by an evil witch.")
        choice4 = st.text_input("The witch offers you a chance to escape if you complete a task. What do you do? (accept/refuse)").strip().lower()

        if choice4 == "accept":
            st.success("🧹 You completed the task and the witch lets you go. You return home safely. The end!")
            if st.button("Restart"):
                st.experimental_rerun()
        elif choice4 == "refuse":
            st.write("🐸 You tried to run and got turned into a frog. Ribbit. The end.")
            if st.button("Restart"):
                st.experimental_rerun()
        elif choice4 != "":
            st.write("That wasn't an option. Your story ends here.")
            if st.button("Restart"):
                st.experimental_rerun()
    elif choice2 != "":
        st.write("That wasn't an option. Your story ends here.")
        if st.button("Restart"):
            st.experimental_rerun()

elif choice1 == "continue":
    st.write("⚡ Bad choice. You got struck by lightning and never made it back home. The end.")
    if st.button("Restart"):
        st.experimental_rerun()

elif choice1 != "":
    st.write("That wasn't an option. Your story ends here.")
    if st.button("Restart"):
        st.experimental_rerun()
