import streamlit as st
from exercises import workout_gen

# Title of the web app
st.title("Workout Generator")

# Generate the workout as you previously did
workout = workout_gen()

# Display the workout in the app
st.header("Today's Workout")
for exercise_type, exercise in workout.items():
    st.write(f"{exercise_type}: {exercise}")