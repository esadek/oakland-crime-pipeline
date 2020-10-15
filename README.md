# Oakland Crime Pipeline
Simple ETL pipeline for crime data from the City of Oakland

## Introduction
To gain a better understanding of the crime in my hometown as well as exercise my data engineering skills, I created a simple pipeline to extract, transform, and load public crime data into a locally hosted database to query. The Oakland Police Department provides crime data from the past 90-days to the public through the City of Oakland’s Crime Watch web site. The dataset can be programmatically accessed via the Socrata Open Data API.

## Dependencies
- [Docker](https://www.docker.com/) OS-level virtualization
- [Python](https://www.python.org/) programming language
- [Prefect](https://www.prefect.io/core) workflow management system
- [Pandas](https://pandas.pydata.org/) data manipulation tool
- [SQLAlchemy](https://www.sqlalchemy.org/) SQL toolkit
- [Sodapy](https://github.com/xmunoz/sodapy) Socrata Open Data API client

## Installation
Clone repository and change directory:
```
$ git clone https://github.com/esadek/oakland-crime-pipeline.git
$ cd oakland-crime-pipeline
```
Build Docker image:
```
$ docker build -t crime-pipeline .
```

## Usage
To execute the pipeline simply run the Docker image:
```
$ docker run crime-pipeline
```

## Credits
Data Provided by [Oakland Police Department](https://www.oaklandca.gov/departments/police)

Dataset Owned by [City of Oakland](https://www.oaklandca.gov/)

## License
[MIT](https://github.com/esadek/oakland-crime-pipeline/blob/master/LICENSE)