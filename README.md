# mysql-bq

This repo is help to export data from MySQL table, then batch load data to Bigquery.

MySQL -> local csv file -> BigQuery

## Install
```
cd mysql-bq
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Prepare
create table in Bigquery

## Run

1. export MySQL env
```
export host=x.x.x.x
export user=mysql_user
export password=mysql_password
export db=mysql_db
```

2. modify parameters

open main.py, modify file_path, table_id and sql_command

3. run
```
python main.py
```
![image](https://user-images.githubusercontent.com/8756642/212266818-5444a0e9-eb2c-4275-bfe1-305e18a1d427.png)


## Check
Open Bigquery to check table data
