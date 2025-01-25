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
