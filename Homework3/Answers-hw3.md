## Steps to load data into GCP

I use the Python script to load data. 

First I install GCP and check if the installation is sucessful 
```ssh
pip install google-cloud-storage
```

```ssh
python3 -c "import google.cloud.storage; print('google-cloud-storage is installed!')"
```

then run the below command to run the python script to download and load data
```ssh
python3 /Users/yitian66/Documents/DE-Datacamp/Homework3/load_yellow_taxi_data_2024.py
```

and then I run below query to create external and regular tables:

```sql
CREATE OR REPLACE EXTERNAL TABLE `modified-alloy-447921-n7.demo_dataset_hw3.yellow_taxi_external`

OPTIONS (
  format = 'PARQUET',
  uris = ['gs://bucket-modified-alloy-447921-n7/yellow_tripdata_2024-*.parquet']
);

CREATE OR REPLACE TABLE `modified-alloy-447921-n7.demo_dataset_hw3.yellow_taxi_table`
AS
SELECT * FROM `modified-alloy-447921-n7.demo_dataset_hw3.yellow_taxi_external`;
```

## Question 1
Then I run below query to count records of 2024 yellow taxi， the count is **20,332,093**:

```sql
select count(*) from `demo_dataset_hw3.yellow_taxi_table`
```
## Question 2
I run below two queries to count distinct PULocationID:
```sql
select count(distinct PULocationID) from demo_dataset_hw3.yellow_taxi_external
```

```sql
select count(distinct PULocationID) from demo_dataset_hw3.yellow_taxi_table
```

and then I check information under job information. 

**0 MB for the External Table and 155.12 MB for the Materialized Table**
