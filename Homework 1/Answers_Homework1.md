

# Table of contents

- [Question 1. Question 1. Understanding docker first run](#Question-1-Understanding-docker-first-run)
- [Question 2. Understanding docker first run](#Question-2-Understanding-docker-first-run)
- [Question 3. Trip Segmentation Count](#Question-3-Trip-Segmentation-Count)
- [Question 4. Longest trip for each day](#Question-4-Longest-trip-for-each-day)
- [Question 5. Three biggest pick up Boroughs](#Question-5-Three-biggest-pick-up-Boroughs)
- [Question 6. Largest tip](#Question-6-Largest-tip)

  
## Question 1. Understanding docker first run
I do not have python:3.12.8 image on my docker hub. So I went to the below site to get the dockerfile of building a python:3.12.8 image.  https://github.com/docker-library/python/blob/23c83c5a82646e123df33d056f7dfbe1d78cfc8b/3.12/bookworm/Dockerfile

and then run below command to build an image.
```ssh
docker build -t python:3.18.2 .
```

And then use below command to run python:3.12.8 in an interactive mode and the entrypoint of bash: 
```ssh
docker run -it --entrypoint=bash python:3.12.8
```
and I use `pip list` to check pip version, my verison is 24.3.1

## Question 2. Understanding Docker networking and docker-compose
The hostname and port that pgadmin should use to connect to the postgres database is ***db:5432***.


### Prepare Postgres
### Steps to ingest green taxi trips data

Step 1: create a yaml file(***docker-compose.yaml***) to set up Postgres and pgAdmin so that I can manage the database through web browser.
and then run `docker-compose up -d` to set up postgres

Step 2: Log on to pgAdmin http://localhost:8080 and register a server

Step 3: create a python script (***ingest_data.py***) to automate the process of downloading, tranformaing and loading to postgres. 

Step 4: create a dockerfile (***dockerfile***) to indicate the instructions of creating an docker image.
Run `docker build -t taxi_ingest:v001 . ` to create a docker image

Step 5: run the below command to ingest Green Taxi data

```ssh
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz"

docker run -it \ 
  --network=homework1_default \ 
  taxi_ingest:v001 \ 
  --user=root \ 
  --password=root \ 
  --host=pgdatabase \ 
  --port=5432 \ 
  --db=ny_taxi \ 
  --table_name=green_taxi_trips \ 
  --url="$URL"
```
### ingest zones data
I use jupter to ingest zones data, please see ***ingest_zone_lookup.ipynb***

And check on pgAdmin if datas are loaded properly. 

![image](https://github.com/user-attachments/assets/29fc5643-3a6d-4e11-8d33-4cf92c0cfa84)


## Question 3. Trip Segmentation Count
The count of taxi trips were totally made on September 18th 2019 is ***15612***.

I use the following sql query:

```sql
select count(1)
from green_taxi_trips 
where date(lpep_pickup_datetime)='2019-09-18' and date(lpep_dropoff_datetime)='2019-09-18'

```

## Question 4. Longest trip for each day
The day with longest trip distance is ***2019-09-26***.
I use the following sql query: 

```sql
select
    date(lpep_pickup_datetime) as pickup_date,
    max(trip_distance) as max_distance
from green_taxi_trips
group by date(lpep_pickup_datetime)
order by max_distance desc
limit 1;
```

## Question 5. Three biggest pick up Boroughs
***Brooklyn, Manhattan Queens*** were the three pick up boroughs that had a sum of total_amount superior to 50000.

```sql
with CTE as (
select
    lpep_pickup_datetime,
    total_amount,
	  zpu."Borough" as pickup_borough
from green_taxi_trips t 
left join zones zpu on t."PULocationID" = zpu."LocationID"
where date(lpep_pickup_datetime) ='2019-09-18'
)

select sum(total_amount), pickup_borough
from CTE
group by pickup_borough
having sum(total_amount)>50000;
```
## Question 6. Largest tip
For the passengers picked up in September 2019 in the zone name Astoria ***JFK Airport*** was the drop off zone that had the largest tip.

I use the following sql query: 
```sql
with CTE as (
select
    lpep_pickup_datetime,
    lpep_dropoff_datetime,
    tip_amount,
    zpu."Zone" as pickup_zone,
    zdo."Zone" as dropoff_zone
from green_taxi_trips t 
   left join zones zpu on t."PULocationID" = zpu."LocationID"
   left join zones zdo on t."DOLocationID" = zdo."LocationID"
where extract(month from lpep_pickup_datetime) = 9
and zpu."Zone"='Astoria'
)
select max(tip_amount), dropoff_zone
from CTE
group by dropoff_zone
order by max(tip_amount) desc
limit 1;
```


