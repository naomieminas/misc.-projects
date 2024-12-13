import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import kagglehub

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', None)

path = kagglehub.dataset_download("bushraqurban/world-education-dataset")

local_csv_path = r"C:\Users\naomi\OneDrive - University of Richmond\CS\misc.-projects\world-education-data.xlsx"

try:
    data = pd.read_excel(local_csv_path)
    print(data.head())
    plt.scatter(data["year"], data["school_enrol_primary_pct"])
    plt.show()
except FileNotFoundError:
    print(f"File not found. Please ensure the path {local_csv_path} is correct.")
