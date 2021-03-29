
"""Simle util function as test"""
import pandas as pd


def read_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    df = df[['species', 'culmen_length_mm', 'culmen_depth_mm',
       'flipper_length_mm', 'body_mass_g']]
    df = df.dropna()
    return df

def create_xy(df):
    X = df.iloc[:,1:]
    Y = df.iloc[:,0]
    return X, Y

def add(new_row):
    df = pd.read_csv("data/penguins_size.csv")
    df = clean_data(df)

    df.append({df.columns[0]: new_row[0],
               df.columns[1]: new_row[1],
               df.columns[2]: new_row[2],
               df.columns[3]: new_row[3],
               df.columns[4]: new_row[4]}, ignore_index=True)
    
    df.to_csv("data/penguins_size_update.csv")
