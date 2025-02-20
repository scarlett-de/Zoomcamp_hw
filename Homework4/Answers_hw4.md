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


