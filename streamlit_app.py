import streamlit as st
from exercises import workout_gen

import streamlit as st
from exercises import workout_gen

def display_workout(workout):
    st.header("Today's Workout")
    for exercise_type, exercise_info in workout.items():
        st.subheader(exercise_type)
        st.write(f"{exercise_info['name']}")
        equipment_list = exercise_info['equipment']
        if 'none' in equipment_list:
            st.write("Equipment: Bodyweight only")
        else:
            st.write("Equipment:")
            for item in equipment_list:
                st.write(f"• {item}")
        st.write("")

workout = workout_gen()
display_workout(workout)
