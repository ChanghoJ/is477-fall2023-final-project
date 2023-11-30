# import libraries for profiling
import os
import pandas as pd
from ydata_profiling import ProfileReport

# dataframe preparation
columns = [
    "class", "Alcohol", "Malicacid", 
    "Ash", "Alcalinity_of_ash", "Magnesium", 
    "Total_phenols", "Flavanoids", "Nonflavanoid_phenols",
    "Proanthocyanins", "Color_intensity", "Hue",
    "0D280_0D315_of_diluted_wines", "Proline",
    ]
wine_df = pd.read_csv("data/wine.data", names=columns)

# make sure directory exist
if not os.path.exists('profiling'):
    os.makedirs('profiling', exist_ok=True)

# dataset profiling
profile = ProfileReport(wine_df, title="Profiling Report")
profile.to_file("profiling/report.html")