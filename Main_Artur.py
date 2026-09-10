import pandas as pd

#you might need to adjust the filepath according to your local setup
df = pd.read_csv("module 1/BME_2315_Module1/DataSet/Metadata and Protein Data for Module 1.csv")

for header in df.columns:
    print(header)