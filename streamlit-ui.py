import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

from mylib import model_train
from mylib import util

st.title("Inference and Training of Penguin Classifier.")
mode = ["inference", "training"]

st.sidebar.header("Application Mode.")
mode_choice = st.sidebar.selectbox("What mode do you want to use?", mode)

if mode_choice == "inference":
    st.header("Inference numbers")
    st.write(
        "In this mode, you can input the four required characteristic input number to make a prediction on what species of penguin they come from."
    )
    with open("classifier.pkl", "rb") as f:
        classifier = pickle.load(f)

    culmen_length_mm = st.number_input("culmen length (mm)", value=50.0)
    culmen_depth_mm = st.number_input("culmen depth (mm)", value=19.0)
    flipper_length_mm = st.number_input("flipper length (mm)", value=215.0)
    body_mass_g = st.number_input("body mass (g)", value=4850)

    if st.button("Inference"):
        new_row = [[culmen_length_mm, 
                    culmen_depth_mm, 
                    flipper_length_mm, 
                    body_mass_g]]

        result = classifier.predict(new_row)
        st.header(f"Predicted Penguin Species: {result[0]}")
        # Plot
        df, X, y = util.data_pipeline("data/penguins_size_cleaned.csv")
        #label_choice_1 = st.selectbox("Characteristic 1", X.columns)
        #label_choice_2 = st.selectbox("Characteristic 2", X.columns)
        label_choice_1 = X.columns[0]
        label_choice_2 = X.columns[1]
        new_sample =[culmen_length_mm, 
                    culmen_depth_mm, 
                    flipper_length_mm, 
                    body_mass_g]
        fig = util.visual_plot(df, X, y, new_sample, label_choice_1, label_choice_2)
        st.sidebar.pyplot(fig)
        image_path = "data/"+result[0]+".jpg"
        image = util.show_image(image_path)
        st.sidebar.header("Your Penguin (\")>")
        st.sidebar.image(image, caption='Does this not look like your penguin? Update our model and choose "Train".')
else:
    st.header("Training")
    st.write(
        "In this mode, you will be able to supply a new training data point, and retrain the model."
    )
    culmen_length_mm = st.number_input("culmen length (mm)", value=1.0)
    culmen_depth_mm = st.number_input("culmen depth (mm)", value=1.0)
    flipper_length_mm = st.number_input("flipper length (mm)", value=1.0)
    body_mass_g = st.number_input("body mass (g)", value=1.0)
    Species = st.selectbox("Species", ["Adelie", "Chinstrap", "Gentoo"])

    st.sidebar.header("Training parameters")
    model_choice = st.sidebar.selectbox("Model", ["Random Forest Classifier"])
    hyper_tuning_choice = st.sidebar.selectbox("Hyper parameter tuning?", [True, False])

    image_path = "data/"+Species+".jpg"
    image = util.show_image(image_path)
    st.sidebar.image(image, caption='Is this the Species you had in mind?')

    if st.button("Train"):
        with st.spinner("Training the model..."):
            new_row = [
                Species,
                culmen_length_mm,
                culmen_depth_mm,
                flipper_length_mm,
                body_mass_g,
            ]
            util.add("data/penguins_size_cleaned.csv",new_row)
            # Here the new data should be inserted
            df, X, y = util.data_pipeline("data/penguins_size_cleaned.csv")
            model, score = model_train.train(
                X, y, hyper_tuning_choice, 5
            )
            st.success(f"Model trained! Accuracy reached: {round(score, 4)}")
        st.balloons()
