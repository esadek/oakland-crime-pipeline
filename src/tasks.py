import pandas as pd
from datetime import date, timedelta
from sqlalchemy import create_engine
from sodapy import Socrata
from prefect import task

@task
def extract(source, dataset):
    """Retrieve data from Socrata API.

    Parameters:
        source (str): Source domain
        dataset (str): Dataset identifier

    Returns:
        DataFrame: Retrieved dataset
    """
    client = Socrata(source, None)
    results = client.get_all(dataset)
    return pd.DataFrame.from_records(results)

@task
def drop_columns(df, cols):
    """Remove unnecessary columns.

    Parameters:
        df (DataFrame): Pandas DataFrame
        cols (list): Column names

    Returns:
        DataFrame: Resulting dataset
    """
    return df.drop(cols, axis=1)

@task
def constrict_days(df, col, days):
    """Remove entries not from last specified number of days.

    Parameters:
        df (DataFrame): Pandas DataFrame
        col (str): Column name
        days (int): Number of days

    Returns:
        DataFrame: Resulting dataset
    """
    today = str(date.today())
    x_days_ago = str(date.today() - timedelta(days=days))
    return df[(df[col] >= x_days_ago) & (df[col] <= today)]

@task
def convert_datetime(df, col):
    """Convert column to type datetime.

    Parameters:
        df (DataFrame): Pandas DataFrame
        col (str): Column name

    Returns:
        DataFrame: Resulting dataset
    """
    dataframe = df.copy()
    dataframe[col] = pd.to_datetime(dataframe[col])
    return dataframe

@task
def load(df, db, table):
    """Load data into SQLite database.

    Parameters:
        df (DataFrame): Pandas DataFrame
        db (str): Database URL
        table (str): Table name
    """
    engine = create_engine(db)
    connection = engine.connect()
    df.to_sql(table, connection)
    connection.close()