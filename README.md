[![Python application test with Github Actions](https://github.com/TimoKerr/realtime-training/actions/workflows/main.yml/badge.svg)](https://github.com/TimoKerr/realtime-training/actions/workflows/main.yml)

# Streamlit Deployed App
https://share.streamlit.io/timokerr/realtime-training/main/streamlit-ui.py

# Real Time Training
This project investigates the possibilities of small-scale real-time model training and serving. Initially only with a Streamlit front-end, but will later add FastAPI backend.

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