## Question 1: Install Spark and PySpark
install pyspark
`pip install pyspark`

Install Java
`brew install openjdk@11`

run `pyspark` in terminal 

then I run `spark.version`, the output is: **'3.5.4'**

## Question 2: Yellow October 2024

I use th below code to download and repartition the Dataframe to 4 partitions and save it to parquet.

```python
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()
!wget -O yellow_tripdata_2024-10.parquet "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-10.parquet"

spark = SparkSession.builder \
    .appName("Read Parquet") \
    .getOrCreate()

df = spark.read.parquet("yellow_tripdata_2024-10.parquet")
df.show(5)

df.schema

df=df.repartition(4)

df.write.parquet('yellow_tripdata/2024/10/')
```
Then I check the file size, which is as below, closed to **25mb**
![image](https://github.com/user-attachments/assets/95a0d1c1-014e-426f-843c-610f2ff4f0c2)


## Question 3: Count records
```python
from pyspark.sql.functions import col

df.filter(col("pickup_date") == "2024-10-15").count()
```
There were **128893** taxi trips on the 15th of October

## Question 4: Longest trip
```python
df_with_diff = df.withColumn(
    "hours_diff", 
    (f.unix_timestamp("tpep_dropoff_datetime") - f.unix_timestamp("tpep_pickup_datetime")) / 3600
)

df_with_diff.agg(f.max("hours_diff").alias("max_duration_hours")).show()
```
The length of the longest trip in the dataset was **162** hours.

## Question 5: User Interface
Local port 4040 shows the application's dashboard on Spark’s User Interface. 

## Question 6: Least frequent pickup location zone
```python
!wget -O zone_lookup.csv "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

df_zones = spark.read \
    .option("header", "true") \
    .csv('zone_lookup.csv')

df_zones.show(5)

df_joined = df.join(df_zones, df.PULocationID == df_zones.LocationID, "left")
df_joined.groupby("Zone").count().orderBy("count").show(1)
```
**Governor's Island/Ellis Island/Liberty Island** is the LEAST frequent pickup location Zone.
