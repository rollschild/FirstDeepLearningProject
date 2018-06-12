import fetch_housing_data as fhd
import os
import pandas as pd

def load_housing_data(housing_path = fhd.HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path) 
    # returns Pandas DataFrame object containing all data
