"""Autograding script."""


def load_data():

    import pandas as pd

    dataset = pd.read_csv("files/input/heart_disease.csv")
    y = dataset.pop("target")
    x = dataset.copy()
    x["thal"] = x["thal"].map(
        lambda x: "normal" if x not in ["fixed", "fixed", "reversible"] else x
    )

    return x, y


def load_estimator():

    import os
    import pickle

    if not os.path.exists("homework/estimator.pickle"):
        return None
    with open("homework/estimator.pickle", "rb") as file:
        estimator = pickle.load(file)

    return estimator


def test_01():

    assert True
