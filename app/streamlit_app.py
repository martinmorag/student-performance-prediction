import streamlit as st
import pandas as pd
from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

exam_model = joblib.load(
    BASE_DIR / "models" / "exam_score_model.pkl"
)

placement_model = joblib.load(
    BASE_DIR / "models" / "placement_model.pkl"
)

st.title(
    "Student Performance Predictor"
)

st.write(
    """
    Predict exam scores and placement outcomes
    based on student academic behavior.
    """
)

study_hours = st.slider(
    "Study Hours",
    min_value=0,
    max_value=12,
    value=6
)

attendance = st.slider(
    "Attendance (%)",
    0,
    100,
    80
)

sleep_hours = st.slider(
    "Sleep Hours",
    0,
    12,
    7
)

internet_usage = st.slider(
    "Internet Usage (hours)",
    0,
    15,
    4
)

assignments_completed = st.slider(
    "Assignments Completed",
    0,
    10,
    8
)

previous_score = st.slider(
    "Previous Score",
    0,
    100,
    70
)

input_df = pd.DataFrame({
    "study_hours": [study_hours],
    "attendance": [attendance],
    "sleep_hours": [sleep_hours],
    "internet_usage": [internet_usage],
    "assignments_completed": [assignments_completed],
    "previous_score": [previous_score]
})

predicted_score = exam_model.predict(
    input_df
)[0]

placement_prediction = placement_model.predict(
    input_df
)[0]

placement_probability = (
    placement_model
    .predict_proba(input_df)[0][1]
)

st.subheader("Results")

st.metric(
    "Predicted Exam Score",
    f"{predicted_score:.1f}"
)

st.metric(
    "Placement Probability",
    f"{placement_probability:.1%}"
)

if placement_prediction == 1:
    st.success("Placed")
else:
    st.error("Not Placed")