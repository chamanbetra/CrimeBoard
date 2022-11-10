#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
# client = Socrata("data.cityofnewyork.us", None)

# Example authenticated client (needed for non-public datasets):
MyAppToken = "uy31BMUiTPtOGaAzhZkjoevas"
client = Socrata("data.cityofnewyork.us",
                 MyAppToken,
                 username="ahmed.say@northeastern.edu",
                 password="Sa@260698")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("qgea-i56i", limit=50000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results).drop([':@computed_region_efsh_h5xi',':@computed_region_f5dn_yrer', ':@computed_region_yeji_bk3q',
                                                    ':@computed_region_92fq_4b7q', ':@computed_region_sbqj_enih'], axis=1)
# print(results_df.head(1))
print("Columns in the data fetched : \n")
columns = results_df.columns
print(columns)
print(columns.__len__())





