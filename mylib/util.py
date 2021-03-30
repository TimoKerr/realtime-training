"""Simle util function as test"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

def data_pipeline(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna()
    df = df[
        [
            "species",
            "culmen_length_mm",
            "culmen_depth_mm",
            "flipper_length_mm",
            "body_mass_g",
        ]
    ]

    X = df.iloc[:, 1:]
    y = df.iloc[:, 0]

    df.to_csv("data/penguins_size_cleaned.csv", index=False)

    return df, X, y


def add(file_path, new_row):
    ''' Assumes new row cols map to old_df cols'''
    
    df_old = pd.read_csv(file_path)
    df = df_old.append(
        {
            df_old.columns[0]: new_row[0],
            df_old.columns[1]: new_row[1],
            df_old.columns[2]: new_row[2],
            df_old.columns[3]: new_row[3],
            df_old.columns[4]: new_row[4],
        },
        ignore_index=True,
    )

    df.to_csv("data/penguins_size_update.csv", index=False)


def visual_plot(df, X, y, new_row, label_1, label_2):
    
    x_1 = X[label_1]
    x_2 = X[label_2]



    x_1_new = new_row[X.columns.get_loc(label_1)]
    x_2_new = new_row[X.columns.get_loc(label_2)]

    fig = plt.figure()
    plt.scatter(x_1, x_2, c=pd.Categorical(y).codes, alpha = 0.4)
    plt.scatter(x_1_new, x_2_new, c="red")
    plt.xlabel(label_1)
    plt.ylabel(label_2)
    plt.title("Where is the sample situated?")
    plt.show()
    return fig

def show_image(image_path):
    image = Image.open(image_path)
    return image

