import unittest
import sys
sys.path.append("../src")
from tasks import drop_columns
import pandas as pd
from prefect import task, Flow

@task
def create_dataframe():
    return pd.DataFrame(columns=['col1', 'col2'])

with Flow('test') as flow:
    test_df = create_dataframe()
    transformed_df = drop_columns(test_df, ['col2'])

class TestDropColumns(unittest.TestCase):
    
    def setUp(self):
        self.state = flow.run()

    def test_drop_columns(self):
        result_df = self.state.result[transformed_df].result
        num_columns = len(result_df.columns)
        self.assertEqual(num_columns, 1)