from mylib import model_train
import pickle
from mylib import util


def test_inference():
    with open("classifier.pkl", "rb") as f:
        classifier = pickle.load(f)
        species = classifier.predict([[12, 34, 22, 1234]])
    return species


def test_train():
    _, X, y = util.data_pipeline("data/penguins_size.csv")
    classifier, score = model_train.train(X, y, True, max_evals=2)
    print(score)
    return classifier, score
