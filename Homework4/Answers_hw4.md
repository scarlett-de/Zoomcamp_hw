## Question 1: Understanding dbt model resolution

The sql model complies to 
```sql
select * from myproject.my_nyc_tripdata.ext_green_taxi

```

## Question 2: dbt Variables & Dynamic Models
```sql
Update the WHERE clause to pickup_datetime >= CURRENT_DATE - INTERVAL '{{ var("days_back", env_var("DAYS_BACK", "30")) }}' DAY
```

Command-line arguments (--vars) take priority

```bash
dbt run --vars '{ "days_back": 7 }'
```

If this is provided, var("days_back") will be 7 and override everything else.

If no command-line argument, check environment variables (env_var()).
```bash
export DAYS_BACK=30
```

If --vars is not provided, env_var("DAYS_BACK") is used.

If neither is set, fall back to the default (30).

## Question 3: dbt Data Lineage and Execution

The below option does not apply for materializing fct_taxi_monthly_zone_revenue:
```ssh
dbt run --select models/staging/+
```

## Question 4: dbt Macros and Jinja

If model_type == 'core', it must use DBT_BIGQUERY_TARGET_DATASET.

If model_type is anything else, it tries DBT_BIGQUERY_STAGING_DATASET but will always fall back to DBT_BIGQUERY_TARGET_DATASET if DBT_BIGQUERY_STAGING_DATASET is not set.

Therefore, the below statements are true to the models using it:

Setting a value for DBT_BIGQUERY_TARGET_DATASET env var is mandatory, or it'll fail to compile

When using core, it materializes in the dataset defined in DBT_BIGQUERY_TARGET_DATASET

When using stg, it materializes in the dataset defined in DBT_BIGQUERY_STAGING_DATASET, or defaults to DBT_BIGQUERY_TARGET_DATASET

When using staging, it materializes in the dataset defined in DBT_BIGQUERY_STAGING_DATASET, or defaults to DBT_BIGQUERY_TARGET_DATASET

## Question 5: Taxi Quarterly Revenue Growth
Please see the quarterly revenue model built, 

then I run the below code 
```sql
SELECT
  pickup_yr_qrt,
  service_type,
  min(yoy_growth_percentage) as min_yoy_growth
FROM
  `dbt-project-451121.dbt_nytaxi.fct_taxi_trips_quarterly_revenue`
  where pickup_yr=2020
  group by pickup_yr_qrt,service_type

  ORDER BY
    min_yoy_growth DESC
```
then the result is: 
**green: {best: 2020/Q1, worst: 2020/Q2}, yellow: {best: 2020/Q1, worst: 2020/Q2}**

## Question 6: P97/P95/P90 Taxi Monthly Fare

Please see fct_taxi_trips_monthly_fare_p95.sql. then I got the below results:

```ssh
green: {p97: 55.0, p95: 45.0, p90: 26.5}, yellow: {p97: 31.5, p95: 25.5, p90: 19.0}
```

## Question 7: Top #Nth longest P90 travel time Location for FHV

Please see then I got the below results, 

For the Trips that respectively started from Newark Airport, SoHo, and Yorkville East, in November 2019, what are dropoff_zones with the 2nd longest p90 trip_duration:
**LaGuardia Airport, Chinatown, Garment District**
