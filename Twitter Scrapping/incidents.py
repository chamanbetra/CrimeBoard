import pandas as pd
from geopy.geocoders import Nominatim
from sqlalchemy import create_engine # for sql related operations
pd.options.mode.chained_assignment = None  # default='warn'

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="passfree",
                               db="crimeboard"))

geolocator = Nominatim(user_agent="geoapiExercises")

data = pd.read_csv('boston_2022.csv', low_memory=False, nrows=10).drop_duplicates()

df1 = []

for i in range(0, len(data)):
    lat = data.iloc[i]['Lat']
    # print(lat)
    long = data.iloc[i]['Long']
    location = geolocator.reverse(lat.astype(str)+","+long.astype(str))

    address = location.raw['address']

    city = address.get('city','')

    df1.append(city)

df2 = pd.DataFrame(df1)
df2.columns=['City']

data = pd.concat([data, df2], axis=1)

data.to_sql('incidents', con=engine, if_exists='append', chunksize=100, index=False)