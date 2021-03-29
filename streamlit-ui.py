import streamlit as st
import pickle

from mylib import model_train
from mylib import util


with open("classifier.pkl", "rb") as f:
    classifier = pickle.load(f)

st.title("Inference and Traning of Penguin Classifier.")
mode = ["inference", "training"]

st.sidebar.header("Application Mode.")
mode_choice = st.sidebar.selectbox("What mode do you want to use?", mode)

if mode_choice == "inference":
    st.header("Inference numbers")
    st.write(
        "In this mode, you can input the four required characteristic input number to make a prediction on what species of penguin they come from."
    )
    culmen_length_mm = st.number_input("culmen_length_mm", value=1)
    culmen_depth_mm = st.number_input("culmen_depth_mm", value=1)
    flipper_length_mm = st.number_input("flipper_length_mm", value=1)
    body_mass_g = st.number_input("body_mass_g", value=1)

    if st.button("Inference"):
        result = classifier.predict(
            [[culmen_length_mm, culmen_depth_mm, flipper_length_mm, body_mass_g]]
        )
        st.write(f"Predicted Penguin Species: {result[0]}")
        # Plot
else:
    st.header("Training")
    st.write(
        "In this mode, you will be able to supply a new training data point, and retrain the model."
    )
    culmen_length_mm = st.number_input("culmen_length_mm", value=1)
    culmen_depth_mm = st.number_input("culmen_depth_mm", value=1)
    flipper_length_mm = st.number_input("flipper_length_mm", value=1)
    body_mass_g = st.number_input("body_mass_g", value=1)
    Species = st.selectbox("Species", ["adelie", "chinstrap", "gentoo"])

    st.sidebar.header("Training parameters")
    model_choice = st.sidebar.selectbox("Model", ["Random Forest Classifier"])
    hyper_tuning_choice = st.sidebar.selectbox("Hyper parameter tuning?", [True, False])

    if st.button("Train"):
        with st.spinner("Training the model..."):
            new_row = [
                Species,
                culmen_length_mm,
                culmen_depth_mm,
                flipper_length_mm,
                body_mass_g,
            ]
            util.add(new_row)
            model, score = model_train.train(
                "data/penguins_size.csv", hyper_tuning_choice, 5
            )
            st.success(f"Model trained! Accuracy reached: {round(score, 4)}")
        st.balloons()
