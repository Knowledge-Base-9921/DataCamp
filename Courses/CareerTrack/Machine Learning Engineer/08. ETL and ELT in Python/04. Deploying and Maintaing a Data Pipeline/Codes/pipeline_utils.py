import pandas as pd

# Define extract, transform and load functions.
 
def extract(file_path):
    return pd.read_csv(file_path)

def transform(raw_data):
    raw_data["average_taxable_income"] = raw_data["total_taxable_income"] / raw_data["number_of_firms"]
    clean_data = raw_data.loc[raw_data["average_taxable_income"] > 100, :]
    clean_data.set_index("industry_name", inplace=True)
    return clean_data

def load(clean_data, clean_data_path):
    clean_data.to_parquet(clean_data_path)