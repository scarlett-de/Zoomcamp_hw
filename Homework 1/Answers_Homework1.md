

# Table of contents

- [Question 1](#question-1)
- [Question 2](#question-2)
- [Question 3](#question-3)

## Question 1

<div style="display: inline-block; width: 45%; vertical-align: top; padding: 10px;">
  <details>
  <summary>Click to see the information I got after run `docker --help`</summary>

```ssh
Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Common Commands:
  run         Create and run a new container from an image
  exec        Execute a command in a running container
  ps          List containers
  build       Build an image from a Dockerfile
  pull        Download an image from a registry
  push        Upload an image to a registry
  images      List images
  login       Authenticate to a registry
  logout      Log out from a registry
  search      Search Docker Hub for images
  version     Show the Docker version information
  info        Display system-wide information

Management Commands:
  ai*         Ask Gordon - Docker Agent
  builder     Manage builds
  buildx*     Docker Buildx
  compose*    Docker Compose
  container   Manage containers
  context     Manage contexts
  debug*      Get a shell into any image or container
  desktop*    Docker Desktop commands (Alpha)
  dev*        Docker Dev Environments
  extension*  Manages Docker extensions
  feedback*   Provide feedback, right in your terminal!
  image       Manage images
  init*       Creates Docker-related starter files for your project
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  plugin      Manage plugins
  sbom*       View the packaged-based Software Bill Of Materials (SBOM) for an image
  scout*      Docker Scout
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Swarm Commands:
  swarm       Manage Swarm

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  import      Import the contents from a tarball to create a filesystem image
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Global Options:
      --config string      Location of client config files (default
                           "/Users/yitian66/.docker")
  -c, --context string     Name of the context to use to connect to the daemon
                           (overrides DOCKER_HOST env var and default context set
                           with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket to connect to
  -l, --log-level string   Set the logging level ("debug", "info", "warn", "error",
                           "fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default
                           "/Users/yitian66/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default
                           "/Users/yitian66/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default
                           "/Users/yitian66/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Run 'docker COMMAND --help' for more information on a command.

For more help on how to use Docker, head to https://docs.docker.com/go/guides/
```
  </details>
</div>

<div style="display: inline-block; width: 45%; vertical-align: top; padding: 10px;">
  <details>
  <summary>Click to see the information I get after I run `docker build --help`</summary>


```ssh
Start a build

Usage:  docker buildx build [OPTIONS] PATH | URL | -

Start a build

Aliases:
  docker build, docker builder build, docker image build, docker buildx b

Options:
      --add-host strings              Add a custom host-to-IP mapping (format:
                                      "host:ip")
      --allow strings                 Allow extra privileged entitlement (e.g.,
                                      "network.host", "security.insecure")
      --annotation stringArray        Add annotation to the image
      --attest stringArray            Attestation parameters (format:
                                      "type=sbom,generator=image")
      --build-arg stringArray         Set build-time variables
      --build-context stringArray     Additional build contexts (e.g., name=path)
      --builder string                Override the configured builder instance
                                      (default "desktop-linux")
      --cache-from stringArray        External cache sources (e.g.,
                                      "user/app:cache", "type=local,src=path/to/dir")
      --cache-to stringArray          Cache export destinations (e.g.,
                                      "user/app:cache", "type=local,dest=path/to/dir")
      --call string                   Set method for evaluating build ("check",
                                      "outline", "targets") (default "build")
      --cgroup-parent string          Set the parent cgroup for the "RUN"
                                      instructions during build
      --check                         Shorthand for "--call=check" (default )
  -D, --debug                         Enable debug logging
  -f, --file string                   Name of the Dockerfile (default:
                                      "PATH/Dockerfile")
      --iidfile string                Write the image ID to a file
      --label stringArray             Set metadata for an image
      --load                          Shorthand for "--output=type=docker"
      --metadata-file string          Write build result metadata to a file
      --network string                Set the networking mode for the "RUN"
                                      instructions during build (default "default")
      --no-cache                      Do not use cache when building the image
      --no-cache-filter stringArray   Do not cache specified stages
  -o, --output stringArray            Output destination (format:
                                      "type=local,dest=path")
      --platform stringArray          Set target platform for build
      --progress string               Set type of progress output ("auto", "plain",
                                      "tty", "rawjson"). Use plain to show
                                      container output (default "auto")
      --provenance string             Shorthand for "--attest=type=provenance"
      --pull                          Always attempt to pull all referenced images
      --push                          Shorthand for "--output=type=registry"
  -q, --quiet                         Suppress the build output and print image ID
                                      on success
      --sbom string                   Shorthand for "--attest=type=sbom"
      --secret stringArray            Secret to expose to the build (format:
                                      "id=mysecret[,src=/local/secret]")
      --shm-size bytes                Shared memory size for build containers
      --ssh stringArray               SSH agent socket or keys to expose to the
                                      build (format:
                                      "default|<id>[=<socket>|<key>[,<key>]]")
  -t, --tag stringArray               Name and optionally a tag (format: "name:tag")
      --target string                 Set the target build stage to build
      --ulimit ulimit                 Ulimit options (default [])

Experimental commands and flags are hidden. Set BUILDX_EXPERIMENTAL=1 to show them.
```
</details>
</div>



<div style="display: inline-block; width: 45%; vertical-align: top; padding: 10px;">
  <details>
  <summary>Click to see the information I got after run `docker run--help`</summary>

```ssh

Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Create and run a new container from an image

Aliases:
  docker container run, docker run

Options:
      --add-host list                    Add a custom host-to-IP mapping
                                         (host:ip)
      --annotation map                   Add an annotation to the
                                         container (passed through to the
                                         OCI runtime) (default map[])
  -a, --attach list                      Attach to STDIN, STDOUT or STDERR
      --blkio-weight uint16              Block IO (relative weight),
                                         between 10 and 1000, or 0 to
                                         disable (default 0)
      --blkio-weight-device list         Block IO weight (relative device
                                         weight) (default [])
      --cap-add list                     Add Linux capabilities
      --cap-drop list                    Drop Linux capabilities
      --cgroup-parent string             Optional parent cgroup for the
                                         container
      --cgroupns string                  Cgroup namespace to use
                                         (host|private)
                                         'host':    Run the container in
                                         the Docker host's cgroup
                                         namespace
                                         'private': Run the container in
                                         its own private cgroup namespace
                                         '':        Use the cgroup
                                         namespace as configured by the
                                                    default-cgroupns-mode
                                         option on the daemon (default)
      --cidfile string                   Write the container ID to the file
      --cpu-period int                   Limit CPU CFS (Completely Fair
                                         Scheduler) period
      --cpu-quota int                    Limit CPU CFS (Completely Fair
                                         Scheduler) quota
      --cpu-rt-period int                Limit CPU real-time period in
                                         microseconds
      --cpu-rt-runtime int               Limit CPU real-time runtime in
                                         microseconds
  -c, --cpu-shares int                   CPU shares (relative weight)
      --cpus decimal                     Number of CPUs
      --cpuset-cpus string               CPUs in which to allow execution
                                         (0-3, 0,1)
      --cpuset-mems string               MEMs in which to allow execution
                                         (0-3, 0,1)
  -d, --detach                           Run container in background and
                                         print container ID
      --detach-keys string               Override the key sequence for
                                         detaching a container
      --device list                      Add a host device to the container
      --device-cgroup-rule list          Add a rule to the cgroup allowed
                                         devices list
      --device-read-bps list             Limit read rate (bytes per
                                         second) from a device (default [])
      --device-read-iops list            Limit read rate (IO per second)
                                         from a device (default [])
      --device-write-bps list            Limit write rate (bytes per
                                         second) to a device (default [])
      --device-write-iops list           Limit write rate (IO per second)
                                         to a device (default [])
      --disable-content-trust            Skip image verification (default
                                         true)
      --dns list                         Set custom DNS servers
      --dns-option list                  Set DNS options
      --dns-search list                  Set custom DNS search domains
      --domainname string                Container NIS domain name
      --entrypoint string                Overwrite the default ENTRYPOINT
                                         of the image
  -e, --env list                         Set environment variables
      --env-file list                    Read in a file of environment
                                         variables
      --expose list                      Expose a port or a range of ports
      --gpus gpu-request                 GPU devices to add to the
                                         container ('all' to pass all GPUs)
      --group-add list                   Add additional groups to join
      --health-cmd string                Command to run to check health
      --health-interval duration         Time between running the check
                                         (ms|s|m|h) (default 0s)
      --health-retries int               Consecutive failures needed to
                                         report unhealthy
      --health-start-interval duration   Time between running the check
                                         during the start period
                                         (ms|s|m|h) (default 0s)
      --health-start-period duration     Start period for the container
                                         to initialize before starting
                                         health-retries countdown
                                         (ms|s|m|h) (default 0s)
      --health-timeout duration          Maximum time to allow one check
                                         to run (ms|s|m|h) (default 0s)
      --help                             Print usage
  -h, --hostname string                  Container host name
      --init                             Run an init inside the container
                                         that forwards signals and reaps
                                         processes
  -i, --interactive                      Keep STDIN open even if not attached
      --ip string                        IPv4 address (e.g., 172.30.100.104)
      --ip6 string                       IPv6 address (e.g., 2001:db8::33)
      --ipc string                       IPC mode to use
      --isolation string                 Container isolation technology
      --kernel-memory bytes              Kernel memory limit
  -l, --label list                       Set meta data on a container
      --label-file list                  Read in a line delimited file of
                                         labels
      --link list                        Add link to another container
      --link-local-ip list               Container IPv4/IPv6 link-local
                                         addresses
      --log-driver string                Logging driver for the container
      --log-opt list                     Log driver options
      --mac-address string               Container MAC address (e.g.,
                                         92:d0:c6:0a:29:33)
  -m, --memory bytes                     Memory limit
      --memory-reservation bytes         Memory soft limit
      --memory-swap bytes                Swap limit equal to memory plus
                                         swap: '-1' to enable unlimited swap
      --memory-swappiness int            Tune container memory swappiness
                                         (0 to 100) (default -1)
      --mount mount                      Attach a filesystem mount to the
                                         container
      --name string                      Assign a name to the container
      --network network                  Connect a container to a network
      --network-alias list               Add network-scoped alias for the
                                         container
      --no-healthcheck                   Disable any container-specified
                                         HEALTHCHECK
      --oom-kill-disable                 Disable OOM Killer
      --oom-score-adj int                Tune host's OOM preferences
                                         (-1000 to 1000)
      --pid string                       PID namespace to use
      --pids-limit int                   Tune container pids limit (set
                                         -1 for unlimited)
      --platform string                  Set platform if server is
                                         multi-platform capable
      --privileged                       Give extended privileges to this
                                         container
  -p, --publish list                     Publish a container's port(s) to
                                         the host
  -P, --publish-all                      Publish all exposed ports to
                                         random ports
      --pull string                      Pull image before running
                                         ("always", "missing", "never")
                                         (default "missing")
  -q, --quiet                            Suppress the pull output
      --read-only                        Mount the container's root
                                         filesystem as read only
      --restart string                   Restart policy to apply when a
                                         container exits (default "no")
      --rm                               Automatically remove the
                                         container and its associated
                                         anonymous volumes when it exits
      --runtime string                   Runtime to use for this container
      --security-opt list                Security Options
      --shm-size bytes                   Size of /dev/shm
      --sig-proxy                        Proxy received signals to the
                                         process (default true)
      --stop-signal string               Signal to stop the container
      --stop-timeout int                 Timeout (in seconds) to stop a
                                         container
      --storage-opt list                 Storage driver options for the
                                         container
      --sysctl map                       Sysctl options (default map[])
      --tmpfs list                       Mount a tmpfs directory
  -t, --tty                              Allocate a pseudo-TTY
      --ulimit ulimit                    Ulimit options (default [])
  -u, --user string                      Username or UID (format:
                                         <name|uid>[:<group|gid>])
      --userns string                    User namespace to use
      --uts string                       UTS namespace to use
  -v, --volume list                      Bind mount a volume
      --volume-driver string             Optional volume driver for the
                                         container
      --volumes-from list                Mount volumes from the specified
                                         container(s)
  -w, --workdir string                   Working directory inside the
                                         container
```
 </details>
</div>

***`--rm` is the one shows Automatically remove the container when it exits***


## Question 2

I run python:3.9 in an interactive mode and the entrypoint of bash using the following command: 
```ssh
docker run -it --entrypoint=bash python:3.9
```
and I use `pip list` to check wheel version, my verison is 0.44.0. 


### Steps to ingest green taxi trips data

Step 1: create a yaml file(***docker-compose.yaml***) to set up Postgres and pgAdmin so that I can manage the database through web browser.
and then run `docker-compose up -d` to set up postgres

Step 2: Log on to pgAdmin http://localhost:8080 and register a server

Step 3: create a python script (***ingest_data.py***) to automate the process of downloading, tranformaing and loading to postgres. 

Step 4: create a dockerfile (***dockerfile***) to indicate the instructions of creating an docker image.
Run `docker build -t taxi_ingest:v001 . ` to create a docker image

Step 5: run the below command to ingest Green Taxi data

```ssh
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"

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

And check on pgAdmin if data loaded properly. 
![image](https://github.com/user-attachments/assets/29fc5643-3a6d-4e11-8d33-4cf92c0cfa84)


## Question 3
The count of taxi trips were totally made on September 18th 2019 is ***15612***.

```sql
select count(1) from green_taxi_trips 
where date(lpep_pickup_datetime)='2019-09-18' and date(lpep_dropoff_datetime)='2019-09-18'
```


I use the following code to get the count:

```sql
select count(1) from green_taxi_trips 
where date(lpep_pickup_datetime)='2019-09-18' and date(lpep_dropoff_datetime)='2019-09-18'
```
