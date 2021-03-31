[![Python application test with Github Actions](https://github.com/TimoKerr/realtime-training/actions/workflows/main.yml/badge.svg)](https://github.com/TimoKerr/realtime-training/actions/workflows/main.yml)

# Streamlit Deployed App
https://share.streamlit.io/timokerr/realtime-training/main/streamlit-ui.py

# Real Time Training
This project looks at Streamlit as a framework to experiment with Proof Of Concept (PoC) Machine Learning Applications. For now, only Streamlit is used for the full functionality (backend and frontend). However, it is possible to use Streamlit as frontend only, and implement the backend in FastAPI (This will be added later on).  

The application itself incorporates both inference (prediction) and training of a classification model to classify Penguin Species. Given input features (measures of the penguin such as flipper size), the model outputs one of three different species. The underlying classifier is a Random Forest Classifier.  

Feedback and real-time training: Together with the predicted species, the application shows a picture of a penguin belonging to the predicted species. This serves as a check, and if the used notices that the model made the wrong prediction, he or she can use the *training* functionality to use their sample as a new training sample, update the dataset and re-train the model. The re-training can be chosen to be with or without hyperparameter optimization.  

# Virtual Environment
```python3 -m venv ~/.realtime-training```  
```source ~/.realtime-training/bin/activate```

# Structure
- streamlit-ui.py contains the front-end interactive code to be run with ```streamlit run streamlit-ui.py```. Here, the user can choose between either making an inference with the pretrained model, or fine-tune the model by providing an extra sample, which is appended to the dataset and saved.  
For training, the user can choose to either do hyperparameter optimization or not.
- mylib contains the files for hyperparameter optimization, data cleaning, and model traning.
- app.py and app_test.py will be used later to introduce the FastAPI backend.
- model.ipynb is a play-notebook for rapid testing.  
  
```
├── app.py
├── app_test.py
├── classifier.pkl
├── data
│   ├── Adelie.jpg
│   ├── Chinstrap.jpg
│   ├── Gentoo.jpg
│   ├── penguins_size_cleaned.csv
│   ├── penguins_size.csv
│   └── penguins_size_update.csv
├── Makefile
├── model.ipynb
├── mylib
│   ├── hyperoptimize.py
│   ├── __init__.py
│   ├── model_train.py
│   └── util.py
├── README.md
├── requirements.txt
└── streamlit-ui.py

```