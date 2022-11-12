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
df2 = []
df3 = []
df4 = []
df5 = []
df6 = []
df7 = []

for i in range(0, len(data)):
    lat = data.iloc[i]['Lat']
    long = data.iloc[i]['Long']
    location = geolocator.reverse(lat.astype(str)+","+long.astype(str))

    address = location.raw['address']

    suburb = address.get('suburb','')
    city = address.get('city','')
    county = address.get('county','')
    state = address.get('state','')
    postcode = address.get('postcode','')
    country = address.get('country','')
    country_code = address.get('country_code','')

    df1.append(suburb)
    df2.append(city)
    df3.append(county)
    df4.append(state)
    df5.append(postcode)
    df6.append(country)
    df7.append(country_code)

dfA1 = pd.DataFrame(df1)
dfA2 = pd.DataFrame(df2)
dfA3 = pd.DataFrame(df3)
dfA4 = pd.DataFrame(df4)
dfA5 = pd.DataFrame(df5)
dfA6 = pd.DataFrame(df6)
dfA7 = pd.DataFrame(df7)

dfA1.columns=['Suburb']
dfA2.columns=['City']
dfA3.columns=['County']
dfA4.columns=['State']
dfA5.columns=['Postcode']
dfA6.columns=['Country']
dfA7.columns=['Country_Code']

data = pd.concat([data, dfA1], axis=1)
data = pd.concat([data, dfA2], axis=1)
data = pd.concat([data, dfA3], axis=1)
data = pd.concat([data, dfA4], axis=1)
data = pd.concat([data, dfA5], axis=1)
data = pd.concat([data, dfA6], axis=1)
data = pd.concat([data, dfA7], axis=1)

data.to_sql('incidents', con=engine, if_exists='append', chunksize=100, index=False)
