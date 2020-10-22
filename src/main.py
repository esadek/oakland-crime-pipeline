from flow import *

# Execute ETL flow
flow.run(
    source_domain = 'data.oaklandnet.com',
    dataset_id = 'ym6k-rx7a',
    to_drop = ['city', 'state', 'location_1', ':@computed_region_w23w_jfhw'],
    column = 'datetime',
    days = 90,
    database = 'sqlite:///database.db',
    table = 'crimes'
)