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

the below statements are true to the models using it:

Setting a value for DBT_BIGQUERY_TARGET_DATASET env var is mandatory, or it'll fail to compile

When using core, it materializes in the dataset defined in DBT_BIGQUERY_TARGET_DATASET

When using stg, it materializes in the dataset defined in DBT_BIGQUERY_STAGING_DATASET, or defaults to DBT_BIGQUERY_TARGET_DATASET

When using staging, it materializes in the dataset defined in DBT_BIGQUERY_STAGING_DATASET, or defaults to DBT_BIGQUERY_TARGET_DATASET

