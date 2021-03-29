from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


from mylib import util
from mylib import hyperoptimize


def train(data_path="data/penguins_size.csv", hyperOpt=bool, max_evals=5):
    """First loads data from data_path, then cleans data, makes x,y and splits.
    The depending on input, hyper parameter optimization will be performed.
    Returns model"""

    df = util.read_data(data_path)
    df = util.clean_data(df)
    X, Y = util.create_xy(df)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=0
    )

    if hyperOpt == True:
        HyperoptSearchResult = hyperoptimize.HyperOptSearch_RFC(
            X_train.values, Y_train.values, max_evals
        )
        # print(HyperoptSearchResult)

        n_estimators = int(HyperoptSearchResult.get("n_estimators"))
        criterion = ["gini", "entropy"][HyperoptSearchResult.get("criterion")]
        max_depth = int(HyperoptSearchResult.get("max_depth"))
        max_features = HyperoptSearchResult.get("max_features")

        classifier = RandomForestClassifier(
            criterion=criterion,
            n_estimators=n_estimators,
            max_depth=max_depth,
            max_features=max_features,
        )
    else:
        classifier = RandomForestClassifier()

    classifier.fit(X_train, Y_train)

    #  Get accuracy
    y_pred = classifier.predict(X_test)
    score = accuracy_score(Y_test, y_pred)

    return classifier, score
