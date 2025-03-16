## set up & process of running command

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

```sql
CREATE TABLE aggregate_events (
     PULocationID INTEGER,
     DOLocationID INTEGER,
     longest_streak INTEGER
);
```

run `docker exec -it redpanda-1 rpk help` and then run `docker exec -it redpanda-1 rpk topic help` to create a topic

run 

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

run `python3 src/producer/producer.py` to send the csv data to kafka. the output is as following:

```ssh
It takes 27.21238684654236 seconds to send the entire dataset and flush
All messages sent to Kafka
```

## Question 5.
Run `docker compose exec jobmanager ./bin/flink run -py /opt/src/job/session.py --pyFiles /opt/src -d` to calculate the longest_streak

the longest_streak is 44 with pick up location id and dropoff location id as 95.
