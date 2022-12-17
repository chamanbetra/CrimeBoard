import pandas as pd
from sqlalchemy import create_engine

incident_url = "incident_dataset.csv"
df_incident = pd.DataFrame(pd.read_csv(incident_url, low_memory=False))

offence_url = "offensecodes.csv"
df_offence_codes = pd.DataFrame(pd.read_csv(offence_url, low_memory=False))

district_loc = "district_code.csv"
df_district_codes = pd.DataFrame(pd.read_csv(district_loc, low_memory=False))

shots_fired_url  = "shots_fired.csv"
df_shots_fired = pd.DataFrame(pd.read_csv(shots_fired_url, low_memory=False))

shooting_url = "shooting.csv"
df_shooting = pd.DataFrame(pd.read_csv(shooting_url, low_memory=False))

firearm_recovery_url = "firearm_recovery.csv"
df_firearm_recovery = pd.DataFrame(pd.read_csv(firearm_recovery_url,  low_memory= False))

print(df_incident.head())
print(df_offence_codes.head())
print(df_district_codes.head())
print(df_shots_fired.head())
print(df_shooting.head())
print(df_firearm_recovery.head())

print(df_shooting.columns)
print(df_incident.columns)

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="1996Ch1609*",
                               db="crimeboard"))
df_offence_codes =  df_offence_codes.drop_duplicates(subset='offense_code', keep="first")
df_offence_codes.to_sql('offense', con=engine, if_exists='append', chunksize=100, index=False)


df_district_codes.to_sql('districts', con=engine, if_exists='append', chunksize=100, index=False)
df_shots_fired['incident_date'] = pd.to_datetime(df_shots_fired['incident_date'])
df_shots_fired.to_sql('shots_fired', con=engine, if_exists='append', chunksize=100, index=False)

df_shooting['shooting_date'] = pd.to_datetime(df_shooting['shooting_date'])

cond_shooting = ~df_shooting['incident_number'].isin(df_incident['incident_number'])
cond_shooting1 = ~df_incident['incident_number'].isin(df_shooting['incident_number'])

df_shooting.drop(df_shooting[cond_shooting].index, inplace=True)
df_incident.drop(df_incident[cond_shooting1].index, inplace=True)

df_shooting.drop_duplicates(subset=['incident_number'], inplace=True)
print(df_shots_fired)


df_shooting.to_sql('shooting', con=engine, if_exists='append', chunksize=100, index=False)

df_incident['occurred_on_date'] = pd.to_datetime(df_incident['occurred_on_date'])
df_incident.to_sql('incidents', con=engine, if_exists='append', chunksize=100, index=False)

df_firearm_recovery.to_sql('firearm_recovery', con=engine, if_exists='append', chunksize=100, index=False)
