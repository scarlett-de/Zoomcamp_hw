# 






# Steps of running the project

## create service account

<img src="https://github.com/user-attachments/assets/4b27bf55-5104-48ef-8a59-7455e02e3831" alt="image" width="500">

<img src="https://github.com/user-attachments/assets/a61ff11a-6312-4d6d-9afa-1e45ad3c0f64" alt="image" width="500">

Cloud storage -> Sotrage Admin

BigQuery -> BigQuery Admin

Compute Engine -> Compute Admin

## Manage Keys

<img src="https://github.com/user-attachments/assets/438e8cae-fed9-4652-ab5b-b1574a57d52c" alt="image" width="500">

<img src="https://github.com/user-attachments/assets/021d74c9-a255-46e8-9ad2-9cd9fcc3fb01" alt="image" width="500">

a json file with your keys will be downloaded, save it to the key folder

## Create Bucket

<img src="https://github.com/user-attachments/assets/bbf00993-43b0-412f-a623-0edf95db822c" alt="image" width="500">


## Create Dataset
Go to big query, and create datasets

## or create using Terraform by setting bucket and dataset name, see the terraform foler
I create three datasets, raw_dataset, staging_dataset and analytics_dataset to save tables in different stages

I save raw data in raw_dataset and save transformed data in staging_dataset, and save the data that is ready for analysis in analytics_dataset. 

then run `terraform init` `terraform plan -out=tfplan` and `terraform apply tfplan`

# Step 2: Load data from Kaggle to GCP and big query

not sure how to download frim kaggle automatically, will try to figure out later. 

create load.py to load csv data to gcs and create regular table in big_query.

# Step 3: dbt transformation

1. run `pip install dbt-core` to install dbt core
   
   and run `pip install dbt-bigquery`
   
   run `export GOOGLE_APPLICATION_CREDENTIALS="/Users/yitian66/Documents/DE-Datacamp/Project/terraform/keys/my_creds.json`

3. Inside the project directory, create the necessary directories and files for your DBT project. 
```ssh
mkdir models
mkdir analysis
mkdir macros
mkdir snapshots
mkdir seeds
mkdir tests
touch dbt_project.yml
touch profiles.yml
```

3. create `profiles.yml` which specifies big query info, like credentials, project_id, bucket_names, dataset names.
   
It contains the configuration information that DBT uses to connect to your database (e.g., BigQuery). It defines connection details like credentials, database names, and project-specific settings. It’s typically located in the ~/.dbt/ directory.


4. create `dbt_project.yml` to configure dbt project name and models, which also state big query dataset/schema that will load staging and analytics tables in.

5. the sql files saved in staging and core folders will be the table names loaded to big query.

6. `dbt run -m core`

# Step 4 create dashboard

![image](https://github.com/user-attachments/assets/17ea41de-420d-464c-9cd2-211226cb5065)

![image](https://github.com/user-attachments/assets/e2a2dac4-cda2-49d1-b677-134aac985f49)

![image](https://github.com/user-attachments/assets/694bbdf7-5037-42e5-9119-bb5091e684a2)

# Step 5: workflow orchestration

`pip install apache-airflow apache-airflow-providers-google dbt`

`pip install apache-airflow-providers-google`

`pip install apache-airflow==2.6.1 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.6.1/constraints-3.11.txt"`

`airflow db init`


```ssh
airflow users create
  --username admin
  --firstname dezoomcamp
  --lastname ww
  --role Admin
  --email ytwyolo66@gmail.com 
  --password dezoomcamp  
  ```

  `airflow webserver --port 8080`

access ariflow web UI



