import unittest
import sys
sys.path.append("../src")
from tasks import drop_columns
import pandas as pd
from prefect import task, Flow

@task
def create_dataframe():
    return pd.DataFrame(columns=['foo', 'bar'])

with Flow('test') as flow:
    test_df = create_dataframe()
    transformed_df = drop_columns(test_df, ['bar'])

class TestDropColumns(unittest.TestCase):
    
    def test_drop_columns(self):
        state = flow.run()
        result_df = state.result[transformed_df].result
        num_result_df_columns = len(result_df.columns)
        self.assertEqual(num_result_df_columns, 1)