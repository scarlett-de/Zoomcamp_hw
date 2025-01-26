## Question 1
I commented out purge files in the example yaml file, and use the one attached (02_postgres_taxi.yml) to ingest yellow_tripdata_2020-12.csv. 
and I checked logs in the executions, the file size is **128.3MB**. 

<img width="688" alt="Screenshot 2025-01-24 at 9 45 13 PM" src="https://github.com/user-attachments/assets/8c0be769-84bd-4371-8a88-c51128c73f3e" />


## Question 2 
The file name should be **green_tripdata_2020-04.csv**.


## Question 3
I use the following sql to count Yellow Taxi data for all CSV files in the year 2020.
There are **24,648,499** rows in total.

```sql
SELECT COUNT(*)
FROM yellow_tripdata
WHERE filename LIKE 'yellow_tripdata_2020-%';
```

## Question 4
I used the 02_postgres_taxi_scheduled.yml to ingest green taxi data. I clicked on Backfill executions, and selected date from 2020-01-01 to 2020-12-31 and then executed. 
![image](https://github.com/user-attachments/assets/0985b629-3f77-4a79-bc40-bb9abc2d3f98)

Then I ran the following sql code:
```sql
SELECT COUNT(*)
FROM green_tripdata
WHERE filename LIKE 'green_tripdata_2020-%';
```
There are 1,734,051 rows for the Green Taxi data for all CSV files in the year 2020.

## Question 5
I use the following sql to count Yellow Taxi data for the March 2021 CSV file.
There are 1,925,152 rows.

```sql
SELECT COUNT(*)
FROM yellow_tripdata
WHERE filename = 'yellow_tripdata_2021-03.csv';
```

## Question 6
Add a timezone property set to **America/New_York** in the Schedule trigger configuration
