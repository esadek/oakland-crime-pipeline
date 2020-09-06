# Oakland Crime Pipeline
> Simple ETL pipeline for crime data from the City of Oakland.

### Table of Contents
- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Author](#author)
- [License](#license)

## Introduction
To gain a better understanding of the crime in my hometown as well as exercise my data engineering skills, I created a simple pipeline to extract, transform, and load public crime data into a locally hosted database to query.

The Oakland Police Department provides crime data from the past 90-days to the public through the City of Oakland’s Crime Watch web site. The dataset can be programmatically accessed via the Socrata Open Data API (SODA).

## Dependencies
- [Python](https://www.python.org/)
- [Prefect](https://www.prefect.io/core)
- [Pandas](https://pandas.pydata.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Sodapy](https://github.com/xmunoz/sodapy)

## Installation
Clone repository and change directory:
```
$ git clone https://github.com/esadek/oakland-crime-pipeline.git
$ cd oakland-crime-pipeline
```
Create virtual environment and install dependencies:
```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

## Usage
To execute the pipeline simply run the etl file:
```
$ python3 etl.py
```

## Author
**Emil Sadek**
[GitHub](https://github.com/esadek)
[LinkedIn](https://www.linkedin.com/in/emil-sadek/)

## License
[MIT](https://github.com/esadek/oakland-crime-pipeline/blob/master/LICENSE)