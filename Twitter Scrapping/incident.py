import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
from geopy.geocoders import Nominatim
from sqlalchemy import create_engine # for sql related operations

# conn = MySQLdb.connect(host="127.0.0.1", user="root", password="Passfree@123", database="Crime_Board")

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="1996Ch1609*",
                               db="crimeboard"))

geolocator = Nominatim(user_agent="geoapiExercises")
# cursor = conn.cursor()
data = pd.read_csv('incident_dataset.csv', low_memory=False, nrows=100).drop_duplicates()
for i in range(0, len(data)):
    lat = data.iloc[i]['Lat']
    long = data.iloc[i]['Long']
    location = geolocator.reverse(lat.astype(str)+","+long.astype(str))

# boston_url = "https://data.boston.gov/dataset/6220d948-eae2-4e4b-8723-2dc8e67722a3/resource/313e56df-6d77-49d2-9c49-ee411f10cf58/download/tmpobugbywv.csv"
#
# boston_data = pd.read_csv(boston_url, low_memory=False)
#
# data_columns = ['INCIDENT_NUMBER', 'OFFENSE_CODE', 'OFFENSE_CODE_GROUP', 'OFFENSE_DESCRIPTION', 'DISTRICT', 'REPORTING_AREA', 'SHOOTING', 'OCCURRED_ON_DATE', 'YEAR', 'MONTH', 'DAY_OF_WEEK', 'HOUR', 'UCR_PART', 'STREET', 'Lat', 'Long', 'Location']
#
# # data_columns = ['incident_number', 'offense_code', 'offense_code_group', 'offense_description', 'district', 'reporting_area', 'shooting', 'occurred_on_date', 'year', 'month', 'day_of_week', 'hour', 'ucr_part', 'street', 'lat', 'long', 'location']

data.to_sql('incidents', con=engine, if_exists='append', chunksize=100, index=False)

