from mylib import model_train
import pickle

if __name__ == "__main__":
    classifier, score = model_train.train("data/penguins_size.csv", True, max_evals=5)

    print(score)

    # save model
    pickle_out = open("classifier.pkl", "wb")
    pickle.dump(classifier, pickle_out)
    pickle_out.close()
