import pandas as pd
from sodapy import Socrata

boston_url = "https://data.boston.gov/dataset/6220d948-eae2-4e4b-8723-2dc8e67722a3/resource/313e56df-6d77-49d2-9c49-ee411f10cf58/download/tmpobugbywv.csv"
df_master_boston_data = pd.DataFrame(pd.read_csv(boston_url, low_memory=False))

offence_url = 'https://data.boston.gov/dataset/6220d948-eae2-4e4b-8723-2dc8e67722a3/resource/3aeccf51-a231-4555-ba21-74572b4c33d6/download/rmsoffensecodes.xlsx'
df_offence_codes = pd.DataFrame(pd.read_excel(offence_url, engine='openpyxl'))

district_loc = "district_code.csv"
df_district_codes = pd.DataFrame(pd.read_csv('district_code.csv'))

shots_fired_url  = "https://data.boston.gov/dataset/85bb7a19-be41-4c1a-a555-3c68405ffbb9/resource/c1e4e6ac-8a84-4b48-8a23-7b2645a32ede/download/tmpbz2t_4p2.csv"
df_shots_fired = pd.DataFrame(pd.read_csv(shots_fired_url, low_memory=False))

shooting_url = "https://data.boston.gov/dataset/e63a37e1-be79-4722-89e6-9e7e2a3da6d1/resource/73c7e069-701f-4910-986d-b950f46c91a1/download/tmpdvxk0cj5.csv"
df_shooting = pd.DataFrame(pd.read_csv(shooting_url, low_memory=False))

firearm_recovery_url = "https://data.boston.gov/dataset/3937b427-6aa4-4515-b30d-c76771313feb/resource/a3d2260f-8a41-4e95-9134-d14711b0f954/download/tmpy0s9f46e.csv"
df_firearm_recovery = pd.DataFrame(pd.read_csv(firearm_recovery_url,  low_memory= False))

print(df_master_boston_data.head())
print(df_offence_codes.head())
print(df_district_codes.head())





engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="1996Ch1609*",
                               db="crimeboard"))

df_district_codes.to_sql('districts', con=engine, if_exists='append', chunksize=100, index=False)
