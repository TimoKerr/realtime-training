[![Python application test with Github Actions](https://github.com/TimoKerr/realtime-training/actions/workflows/main.yml/badge.svg)](https://github.com/TimoKerr/realtime-training/actions/workflows/main.yml)

# Streamlit-Deployed, ML-powered Application
https://share.streamlit.io/timokerr/realtime-training/main/streamlit-ui.py

# Real Time Training
This project looks at Streamlit as a framework to experiment with Proof Of Concept (PoC) Machine Learning Applications. For now, only Streamlit is used for the full functionality (backend and frontend). However, it is possible to use Streamlit as frontend only, and implement the backend in FastAPI (This will be added later on).  

The application itself incorporates both inference (prediction) and training of a classification model to classify Penguin Species. Given input features (measures of the penguin such as flipper size), the model outputs one of three different species. The underlying classifier is a Random Forest Classifier.  

Feedback and real-time training: Together with the predicted species, the application shows a picture of a penguin belonging to the predicted species. This serves as a check, and if the used notices that the model made the wrong prediction, he or she can use the *training* functionality to use their sample as a new training sample, update the dataset and re-train the model. The re-training can be chosen to be with or without hyperparameter optimization.  

The GitHub repo is also provided with files ensuring good CI/CD practices such as linting, testing, and GitHub actions. What still needs to be implemented is a Docker file or Docker-compose file to containerize the entire application.

# Virtual Environment
Always a good idea to make a virtual environment to avoid package dependency conflicts.  
```python3 -m venv ~/.realtime-training```  
```source ~/.realtime-training/bin/activate```

# Run Application
```make install``` to install necessary packages.  
```streamlit run streamlit-ui.py``` to run the streamlit application. Or since the application is hosted simply visit: https://share.streamlit.io/timokerr/realtime-training/main/streamlit-ui.py  

# Structure and Workings
- *streamlit-ui.py* contains the front-end interactive code to be run with ```streamlit run streamlit-ui.py```. Here, the user can choose between either making an inference with the pretrained model, or fine-tune the model by providing an extra sample, which is appended to the dataset and is saved.  
For training, the user can choose to either do hyperparameter optimization or not.
- */mylib* contains the files for hyperparameter optimization, data cleaning, and model training.
- *mylib/hyperoptimize.py* contains the function for non-trivial hyperparameter optimization for the Random Forest Classfier. The package ```hyperopt``` is used.  
- *mylib/model_train.py* contains the function to actually train the Random Forest Classifier model with either default hyperparameters, or those obtained from the optimization.  
- *mylib/util.py* contains utility functions, of which the *data_pipeline()* is the most important one. It takes in the raw dataframe and output data that is ready to be traned on. Further functions include *add()* to add a sample to the training set, and *visual_plot()* which plots the scatter to situate where the new sample lies.  
- *app.py* and *app_test.py* will be used later to introduce the FastAPI backend.
- *model.ipynb* is a scrap-notebook for rapid testing. 
- *requirements.txt* contains the packages needed. The file is used by the ...  
- *Makefile* to install the packages. The Makefile also contains the necessary tools for CI/CD, using linting, testing, and formatting. 
  
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