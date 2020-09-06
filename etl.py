import pandas as pd
from datetime import date, timedelta
from sqlalchemy import create_engine
from sodapy import Socrata
from prefect import task, Flow, Parameter

@task
def extract(source, dataset):
    '''Retrieve data from Socrata API.'''
    client = Socrata(source, None)
    results = client.get_all(dataset)
    return pd.DataFrame.from_records(results)

@task
def drop_columns(df, cols):
    '''Remove unnecessary columns.'''
    return df.drop(cols, axis=1)

@task
def constrict_days(df, col, days):
    '''Remove entries not from last specified number of days.'''
    today = str(date.today())
    x_days_ago = str(date.today() - timedelta(days=days))
    return df[(df[col] >= x_days_ago) & (df[col] <= today)]

@task
def convert_datetime(df, col):
    '''Convert column to type datetime.'''
    dataframe = df.copy()
    dataframe[col] = pd.to_datetime(dataframe[col])
    return dataframe

@task
def load(df, db, table):
    '''Load data into SQLite database.'''
    engine = create_engine(db)
    connection = engine.connect()
    df.to_sql(table, connection)
    connection.close()

with Flow('ETL') as flow:
    # Parameters
    source_domain = Parameter('source_domain')
    dataset_id = Parameter('dataset_id')
    to_drop = Parameter('to_drop')
    column = Parameter('column')
    days = Parameter('days')
    database = Parameter('database')
    table = Parameter('table')

    # Task dependencies
    extracted = extract(source_domain, dataset_id)
    post_drop = drop_columns(extracted, to_drop)
    constricted = constrict_days(post_drop, column, days)
    converted = convert_datetime(constricted, column)
    loaded = load(converted, database, table)

if __name__ == '__main__':
    # Execute flow
    flow.run(
        source_domain = 'data.oaklandnet.com',
        dataset_id = 'ym6k-rx7a',
        to_drop = ['city', 'state', 'location_1', ':@computed_region_w23w_jfhw'],
        column = 'datetime',
        days = 90,
        database = 'sqlite:///database.db',
        table = 'crimes'
    )