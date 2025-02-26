## Question 1: Install Spark and PySpark
install pyspark
`pip install pyspark`

Install Java
`brew install openjdk@11`

run `pyspark` in terminal 

then I run `spark.version`, the output is: **'3.5.4'**

## Question 2: Yellow October 2024

I use th below code to download and repartition the Dataframe to 4 partitions and save it to parquet.

```pyspark
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
