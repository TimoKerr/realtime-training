from mylib import model_train
import pickle


def test_inference():
    with open("classifier.pkl", "rb") as f:
        classifier = pickle.load(f)
        species = classifier.predict([[12, 34, 22, 1234]])
    return species


def test_train():
    classifier, score = model_train.train("data/penguins_size.csv", True, max_evals=2)
    print(score)
    return classifier, score
