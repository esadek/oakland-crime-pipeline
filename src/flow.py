from tasks import *
from prefect import Flow, Parameter

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