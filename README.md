# Oakland Crime Pipeline
ETL pipeline for crime data from the City of Oakland

### Table of Contents
- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Author](#author)
- [License](#license)

## Introduction

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