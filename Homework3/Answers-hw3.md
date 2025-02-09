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

## Question 3
I run below query to retrive PULocationID, and retrive both PULocationID and DOLocationID:

```sql
select PULocationID from demo_dataset_hw3.yellow_taxi_table
```

```sql
select PULocationID,DOLocationID from demo_dataset_hw3.yellow_taxi_table
```
Bytes processed of above two queries are 155.12 mb, 310.24 mb respectively. 

Reason is BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

## Question 4

I run below query to count records which fare_amount= 0. 
There is **8,333** records that fare_amount is 0. 

```sql
select count(*) from demo_dataset_hw3.yellow_taxi_external where fare_amount=0
```

## Question 5

**Partition by tpep_dropoff_datetime and Cluster on VendorID**. 

Below is the code:

```sql
CREATE OR REPLACE TABLE `demo_dataset_hw3.yellow_taxi_table_partitioned`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID as (
 SELECT * FROM `demo_dataset_hw3.yellow_taxi_table`)
```

## Quesiton 6
Run the below two queries and compare the bytes processed. 

**310.24 MB for non-partitioned table and 26.84 MB for the partitioned table.**

```sql
select distinct VendorID, tpep_dropoff_datetime
from demo_dataset_hw3.yellow_taxi_table
where date(tpep_dropoff_datetime) between '2024-03-01' and '2024-03-15'
```

```sql
select distinct VendorID, tpep_dropoff_datetime
from demo_dataset_hw3.yellow_taxi_table_partitioned
where date(tpep_dropoff_datetime) between '2024-03-01' and '2024-03-15'
```

## Question 7
**GCP Bucket** stores data of external tables. 

## Question 8
**False**

Based on lecture we learned, below are the situations where we should use cluster and its limitations.

- Columns you specify are used to colocate related data
- Order of the column is important
- The order of the specified columns determines the sort order of the data.
- Clustering improves
   - Filter queries
   - Aggregate queries
- Table with data size < 1 GB, don't show significant improvement with partitioning and clustering. May increase costs.
- You can specify up to four clustering columns
- Columns must be top-level col and non-repeated

