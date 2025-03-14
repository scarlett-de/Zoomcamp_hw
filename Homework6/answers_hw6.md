## set up 

docker stop $(docker ps -q)

docker rm $(docker ps -aq)

run `docker compose up --remove-orphans -d` to set up
and then log into pgadmin and create following table 

```SQL
CREATE TABLE processed_events (
    lpep_pickup_datetime VARCHAR,
    lpep_dropoff_datetime VARCHAR,
    PULocationID INT,
    DOLocationID INT,
    passenger_count INT,
    trip_distance NUMERIC,
    tip_amount NUMERIC
);
```
and then create a topic: `docker exec -it redpanda-1 rpk topic create green-trips` 

then run `python3 src/producer/producer.py`

and then run `docker compose exec jobmanager ./bin/flink run -py /opt/src/job/load.py --pyFiles /opt/src -d` to load data to processed_events table


## Question 1: Redpanda version
I run the command `docker exec -it redpanda-1 rpk help` and get the following result:

```ssh
rpk is the Redpanda CLI & toolbox

Usage:
  rpk [flags]
  rpk [command]

Available Commands:
  cloud       Interact with Redpanda cloud
  cluster     Interact with a Redpanda cluster
  connect     A stream processor for mundane tasks - https://docs.redpanda.com/redpanda-connect
  container   Manage a local container cluster
  debug       Debug the local Redpanda process
  generate    Generate a configuration template for related services
  group       Describe, list, and delete consumer groups and manage their offsets
  help        Help about any command
  iotune      Measure filesystem performance and create IO configuration file
  plugin      List, download, update, and remove rpk plugins
  profile     Manage rpk profiles
  redpanda    Interact with a local Redpanda process
  registry    Commands to interact with the schema registry
  security    Manage Redpanda security
  topic       Create, delete, produce to and consume from Redpanda topics
  transform   Develop, deploy and manage Redpanda data transforms
  version     Prints the current rpk and Redpanda version

Flags:
      --config string            Redpanda or rpk config file; default search paths are
                                 "/var/lib/redpanda/.config/rpk/rpk.yaml", $PWD/redpanda.yaml, and
                                 /etc/redpanda/redpanda.yaml
  -X, --config-opt stringArray   Override rpk configuration settings; '-X help' for detail or '-X list' for terser detail
  -h, --help                     Help for rpk
      --profile string           rpk profile to use
  -v, --verbose                  Enable verbose logging
      --version                  version for rpk

Use "rpk [command] --help" for more information about a command.
```

then I run `docker exec -it redpanda-1 rpk version` and get the following:
```ssh
 docker exec -it redpanda-1 rpk version

Version:     v24.2.18
Git ref:     f9a22d4430
Build date:  2025-02-14T12:59:41Z
OS/Arch:     linux/arm64
Go version:  go1.23.1
```

## Question 2. Creating a topic

`docker exec -it redpanda-1 rpk help` and then run `docker exec -it redpanda-1 rpk topic help`
create the topic `docker exec -it redpanda-1 rpk topic create green-trips`

the output is 
```ssh
TOPIC        STATUS
green-trips  OK
```

## Question 3. Connecting to the Kafka server
I run the script, it does not return me anything, so I change the last line to `print(producer.bootstrap_connected())`.

then I get `True` as output which means Kafka is successfully connected.

## Question 4. Sending the Trip Data

```python
file_path = "/Users/yitian66/Documents/DE-Datacamp/Week6/hw6/green_tripdata_2019-10.csv.gz"

df = pd.read_csv(file_path, compression="gzip")

selected_col=['lpep_pickup_datetime',
'lpep_dropoff_datetime',
'PULocationID',
'DOLocationID',
'passenger_count',
'trip_distance',
'tip_amount'
]

new_df=df[selected_col]

print(new_df.head())
```
If I want to see messages sent to Kafka, I can run these commands:
`brew install kafka`

`brew services start kafka`

`kafka-console-consumer --bootstrap-server localhost:9092 --topic green-trips --from-beginning`

`docker compose exec jobmanager ./bin/flink run -py /opt/src/job/3.session.py --pyFiles /opt/src -d`
