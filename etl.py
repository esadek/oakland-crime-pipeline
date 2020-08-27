import pandas as pd
from datetime import date, timedelta
from sqlalchemy import create_engine
from sodapy import Socrata

def constrict_days(df, col, days):
    '''Remove entries not from last specified number of days'''
    today = str(date.today())
    x_days_ago = str(date.today() - timedelta(days=days))
    return df[(df[col] >= x_days_ago) & (df[col] <= today)]

def extract():
    '''Retrieve crime data from Socrata API.'''
    client = Socrata('data.oaklandnet.com', None)
    results = client.get_all('ym6k-rx7a')
    return pd.DataFrame.from_records(results)

def transform(data):
    '''Transform crime data.'''
    to_drop = ['city', 'state', 'location_1', ':@computed_region_w23w_jfhw']
    df = data.drop(to_drop, axis=1)
    df = constrict_days(df, 'datetime', 90)
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

def load(data):
    '''Load crime data into SQLite database.'''
    engine = create_engine('sqlite:///database.db')
    sqlite_connection = engine.connect()
    data.to_sql('crimes', sqlite_connection)
    sqlite_connection.close()

# ETL pipeline
(extract().pipe(transform)
          .pipe(load)
)