## Steps to load data into GCP

I use the Python script to load data. 

First I install GCP and check if the installation is sucessful 
```ssh
pip install google-cloud-storage
```

```ssh
python3 -c "import google.cloud.storage; print('google-cloud-storage is installed!')"
```

then run the below command to run the python script to download and load data
```ssh
python3 /Users/yitian66/Documents/DE-Datacamp/Homework3/load_yellow_taxi_data_2024.py
```
