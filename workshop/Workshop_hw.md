## Install dlt

https://dlthub.com/docs/reference/installation


On macOS, you can use Homebrew to install Python 3.10.
```ssh
brew update
brew install python@3.10
```

Create a new virtual environment in your working folder. This will create an ./env directory where your virtual environment will be stored:
```ssh
python -m venv ./en
```

Activate the virtual environment:
```ssh
source ./env/bin/activate
```
Install dlt library
You can now install dlt in your virtual environment by running:

```ssh
# install the newest dlt version or upgrade the existing version to the newest one
pip install "dlt[duckdb]"
```

install all the necessary dependencies
```ssh
pip install duckdb pandas numpy pyarrow
```

## Question 1. Check dlt version
I ran below code to check dlt version. And the version is **__main__.py 1.6.1**.
```ssh
python3 -m dlt --version
```

## Question 2
I ran the pipeline_dlt.py to load the data. 
There are **4** tables created. 

![image](https://github.com/user-attachments/assets/db41a34e-5bf8-4d51-a39e-6cc4abd4b75d)


## Question 3
I run below code to count the rows, there are **10,000** rows extracted.
```python
data = pipeline.dataset(dataset_type="default").rides.df()
print(len(data))
```

## Question 4
I run the below sql and the average minute is **12.3049**
```python
with pipeline.sql_client() as client:
    res = client.execute_sql(
            """
            SELECT
            AVG(date_diff('minute', trip_pickup_date_time, trip_dropoff_date_time))
            FROM rides;
            """
        )
    # Prints column values of the first row
    print(res)
```
