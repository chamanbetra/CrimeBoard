import pandas as pd
from sodapy import Socrata

boston_url = "https://data.boston.gov/dataset/6220d948-eae2-4e4b-8723-2dc8e67722a3/resource/313e56df-6d77-49d2-9c49-ee411f10cf58/download/tmpobugbywv.csv"
df_master_boston_data = pd.DataFrame(pd.read_csv(boston_url, low_memory=False))

offence_url = 'https://data.boston.gov/dataset/6220d948-eae2-4e4b-8723-2dc8e67722a3/resource/3aeccf51-a231-4555-ba21-74572b4c33d6/download/rmsoffensecodes.xlsx'
df_offence_codes = pd.DataFrame(pd.read_excel(offence_url, engine='openpyxl'))

district_loc = "district_code.csv"
df_district_codes = pd.DataFrame(pd.read_csv('district_code.csv'))

print(df_master_boston_data.head())
print(df_offence_codes.head())
print(df_district_codes.head())





engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="1996Ch1609*",
                               db="crimeboard"))

df_district_codes.to_sql('districts', con=engine, if_exists='append', chunksize=100, index=False)
