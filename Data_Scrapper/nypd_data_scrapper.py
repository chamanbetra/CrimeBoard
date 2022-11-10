import pandas as pd
from sodapy import Socrata

# Example authenticated client (needed for non-public datasets):
MyAppToken = "uy31BMUiTPtOGaAzhZkjoevas"
client = Socrata("data.cityofnewyork.us",
                 MyAppToken,
                 username="ahmed.say@northeastern.edu",
                 password="Sa@260698")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
new_york_results = client.get("qgea-i56i", limit=50000)

# Convert to pandas DataFrame
new_york_results_df = pd.DataFrame.from_records(new_york_results).drop([':@computed_region_efsh_h5xi',':@computed_region_f5dn_yrer', ':@computed_region_yeji_bk3q',
                                                    ':@computed_region_92fq_4b7q', ':@computed_region_sbqj_enih'], axis=1)
# print(results_df.head(1))
print("Columns in the data fetched : \n")

columns = new_york_results_df.columns
print(columns)
print(new_york_results_df.head(5))
print(columns.__len__())

boston_url = "https://data.boston.gov/dataset/6220d948-eae2-4e4b-8723-2dc8e67722a3/resource/313e56df-6d77-49d2-9c49-ee411f10cf58/download/tmpobugbywv.csv"
boston_data = pd.read_csv(boston_url)






