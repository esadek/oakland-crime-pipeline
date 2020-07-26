import pandas as pd
import datetime
from sodapy import Socrata
from prefect import task, Flow
from prefect.tasks.database.sqlite import SQLiteScript


@task
def extract_crime_data():
    client = Socrata('data.oaklandnet.com', None)
    return client.get_all('ym6k-rx7a')


@task
def transform_crime_data(data):
    # Convert data to DataFrame
    df = pd.DataFrame.from_records(data)
    # Rename location column
    df = df.rename(columns={'location_1': 'location'})
    # Drop unnecessary columns
    to_drop = ['city', 'state', ':@computed_region_w23w_jfhw']
    df.drop(to_drop, axis=1, inplace=True)
    # Drop rows not from last 90 days
    today = str(datetime.date.today())
    ninety_days_ago = str(datetime.date.today() - timedelta(days=90))
    df = df[(df['datetime'] >= ninety_days_ago) & (df['datetime'] <= today)]
    return df


@task
def load_crime_data(data):
    pass

with Flow('ETL') as flow:
    e = extract_crime_data()
    t = transform_crime_data(e)
    l = load_crime_data(t)

flow.run()