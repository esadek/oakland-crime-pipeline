import pandas as pd
from sodapy import Socrata
from prefect import task, Flow
from prefect.tasks.database.sqlite import SQLiteScript


@task
def extract_crime_data():
    """Extract JSON crime data from API."""
    client = Socrata('data.oaklandnet.com', None)
    results = client.get_all('ym6k-rx7a')
    return results


@task
def transform_crime_data(data):
    """Transform crime data."""
    df = pd.DataFrame.from_records(data) # Convert data to DataFrame
    df = df.rename(columns={'location_1': 'location'}) # Rename location column
    to_drop = ['city', 'state', ':@computed_region_w23w_jfhw']
    df.drop(to_drop, axis=1, inplace=True) # Drop unnecessary columns
    df = df[df['datetime'].str.startswith('2020')] # Drop rows not from 2020
    df['datetime'] = pd.to_datetime(df['datetime']) # Convert datetime
    return df


@task
def load_crime_data(data):
    """Load crime data into SQLite database."""
    pass

with Flow('ETL') as flow:
    e = extract_crime_data()
    t = transform_crime_data(e)
    l = load_crime_data(t)

flow.run()