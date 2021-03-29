""" Different hyperparameter optimisation methods"""
import numpy as np

# General
from sklearn import ensemble
from sklearn import metrics
from sklearn import model_selection
from functools import partial

# Hyperopt
from hyperopt import hp, fmin, tpe, Trials
from hyperopt.pyll.base import scope
def test():
    works = "Module loaded."
    return works


def HyperOptSearch_RFC(train_x, train_y, max_evals=5):
    """ Using HyperOpt library. Returns dictionary with best Hyper Params"""

    # First define the optimize function
    def optimize(params, x, y):
        model = ensemble.RandomForestClassifier(**params)
        kf = model_selection.StratifiedKFold(n_splits=5)
        accuracies = []
        # split data
        for idx in kf.split(X=x, y=y):
            train_idx, test_idx = idx[0], idx[1]
            xtrain = x[train_idx]
            ytrain = y[train_idx]

            xtest = x[test_idx]
            ytest = y[test_idx]

            model.fit(xtrain, ytrain)
            preds = model.predict(xtest)
            fold_acc = metrics.accuracy_score(ytest, preds)
            accuracies.append(fold_acc)
        # Return the thing to minimize (-1 because lower is better)
        return -1.0 * np.mean(accuracies)

    # Defining param spac enow requires defining a dict
    param_space = {
        "max_depth": scope.int(hp.quniform("max_depth", 3, 15, 1)),
        "n_estimators": scope.int(hp.quniform("n_estimators", 100, 600, 1)),
        "criterion": hp.choice("criterion", ["gini", "entropy"]),
        "max_features": hp.uniform("max_features", 0.01, 1),
    }

    optimization_function = partial(optimize, x=train_x, y=train_y)

    trials = Trials()
    result = fmin(
        fn=optimization_function,
        space=param_space,
        algo=tpe.suggest,
        max_evals=max_evals,
        trials=trials,
    )

    return result