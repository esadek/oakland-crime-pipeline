# Tasks

## extract(*source*, *dataset*)
Retrieve data from Socrata API.

**Parameters:**
- *source* (str): Source domain
- *dataset* (str): Dataset identifier

**Returns:**
- DataFrame: Retrieved dataset

## drop_columns(*df*, *cols*):
Remove unnecessary columns.

**Parameters:**
- *df* (DataFrame): Pandas DataFrame
- *cols* (list): Column names

**Returns:**
- DataFrame: Resulting dataset

## constrict_days(*df*, *col*, *days*):
Remove entries not from last specified number of days.

**Parameters:**
- *df* (DataFrame): Pandas DataFrame
- *col* (str): Column name
- *days* (int): Number of days

**Returns:**
- DataFrame: Resulting dataset

## convert_datetime(*df*, *col*):
Convert column to type datetime.

**Parameters:**
- *df* (DataFrame): Pandas DataFrame
- *col* (str): Column name

**Returns:**
- DataFrame: Resulting dataset

## load(*df*, *db*, *table*):
Load data into SQLite database.

**Parameters:**
- *df* (DataFrame): Pandas DataFrame
- *db* (str): Database URL
- *table* (str): Table name