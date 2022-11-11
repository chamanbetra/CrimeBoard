import pandas as pd
from sqlalchemy import create_engine # for sql related operations
data = pd.read_csv('district_code.csv')
df = pd.DataFrame(data)

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="1996Ch1609*",
                               db="crimeboard"))

df.to_sql('districts', con=engine, if_exists='append', chunksize=100, index=False)

