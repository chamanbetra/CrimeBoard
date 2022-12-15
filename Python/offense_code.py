import pandas as pd
from sqlalchemy import create_engine # for sql related operations
data = pd.read_csv('offensecodes.csv')
df = pd.DataFrame(data).drop_duplicates()

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="1996Ch1609*",
                               db="crimeboard"))

df.to_sql('offense', con=engine, if_exists='append', chunksize=100, index=False)

