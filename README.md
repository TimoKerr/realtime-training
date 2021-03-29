# Real Time Training
This project investigates the possibilities of small-scale real-time model training and serving. Initially only with a Streamlit front-end, but will later add FastAPI backend.

# Virtual Environment
```python3 -m venv ~/.realtime-trainig```\n
```source ~/.realtime-training/bin/activate```

# Building the project
1. Create a simple regression model to regress .csv data in a ```.ipynb``` file (with hyperparameter optimization search)
2. Add two more regressor models to compare resutls.
3. Cast this into Streamlit application for serving.
4. Now incorporate getting new training sample from streamlit to retrain the model.
