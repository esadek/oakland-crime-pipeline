import pandas as pd
from datetime import date, timedelta
from sodapy import Socrata
from prefect import task, Flow
from prefect.tasks.database.sqlite import SQLiteScript

SOURCE_DOMAIN = 'data.oaklandnet.com'
DATASET_IDENTIFIER = 'ym6k-rx7a'

@task
def extract():
    '''Retrieve crime data from Socrata API.'''
    client = Socrata(SOURCE_DOMAIN, None)
    results = client.get_all(DATASET_IDENTIFIER)
    return pd.DataFrame.from_records(results)

@task
def transform(data):
    '''Transform crime data.'''

    # Drop unnecessary columns
    to_drop = ['city', 'state', 'location_1', ':@computed_region_w23w_jfhw']
    df = data.drop(to_drop, axis=1)

    # Drop rows not from last 90 days
    today = str(date.today())
    ninety_days_ago = str(date.today() - timedelta(days=90))
    df = df[(df['datetime'] >= ninety_days_ago) & (df['datetime'] <= today)]

    return df

@task
def load(data):
    '''Load crime data into SQLite database.'''
    pass

with Flow('ETL') as flow:
    e = extract()
    t = transform(e)
    l = load(t)

flow.run()