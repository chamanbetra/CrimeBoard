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
results = client.get("qgea-i56i", limit=20000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
print(results_df.head())