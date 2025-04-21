```bash
# run a docker container in detached (does not keep terminal busy while running) mode, always restart automatically when it is not stopped manually, forward host port 80 to container's port 80, set memory usage limit to 1000M, allocate minimum of 250M (but it can ask for less memory, and that's ok, however the upper limit is 1000M), from image 'nginx:1.18.0'
docker run -d --name <container_name nginx> --restart unless-stopped -p 80:80 \
--memory 1000M --memory-reservation 250M <container_image nginx:1.18.0>`
``` 
---
```bash
# For debugging purposes, create docker container using busybox image (bare minimum OS, and plus contains curl) interactively (go inside of the container after the creation completes), and after we exit from the shell, completely remove the container.
docker run -it --rm --name busybox-test yauritux/busybox-curl:latest
``` 
---
```bash
# list all containers
docker ps -a
``` 
---
```bash
# Check log trace of container
docker logs <container_name OR container_id>
``` 
---
```bash
# Stop a container
docker stop <container_name OR container_id>
``` 
---
```bash
# start a container
docker start <container_name OR container_id>
````
---
```bash
# remove a container
docker rm <container_name OR container_id>
```
---

```bash
# remove a container without the necessity of stopping it
docker rm -f <container_name OR container_id>
``` 
---
```bash
# Watch the status of containers in sync, keeps terminal busy
watch docker ps -a
``` 
---

> [!NOTE] Where Are the Logs of Containers Stored?
> **Note:** The logs of containers are stored in directory: `/var/lib/docker/containers/<container_id>/<container_id>-json.log` ' if the log driver is `json-file` configured in `/etc/docker/daemon.json`. Since containers are ephemeral and once they are deleted, all of its files are also deleted, we need to store the logs in some other place, and it could be splunk, awslogs, gcplogs etc.

```bash
# Deploying containers altogether that are defined in docker-compose.yaml file
docker compose up -d
``` 
---
```bash
# Deleting containers altogether that are defined in docker-compose.yaml file, containing the volumes mounted
docker compose down --volumes
```
---
```bash
# Restarting a service defined in docker-compose.yaml file
docker compose restart <service_name>
``` 

> [!NOTE] What is the Effect of Deleting Volumes in Docker Compose?
> Since we mount the volume of redis into host filesystem, even after we restart the redis service, the data persists there. However, if we use `docker compose down --volumes` then it will be gone ofc, since we are completely deleting the resources.
> 

```bash
# To inspect the image layers that comprises the image.
docker history <image_name:tag>
``` 

> [!NOTE] Why we Do Not Use Sudo in Dockerfile?
> 
> **Note**: In dockerfile, we are not using command `sudo` since all of the commands run as root user by default. 
> 

> [!NOTE] Why apt upgrade is not followed by apt update in Dockerfile?
> Usually, `apt update` followed by the package that needs to be installed will suffice; since `apt upgrade` will upgrade all installed packages, which are not necessary to use. For instance, `apt update && apt install -y curl` will fetch the latest information about available packages, then will install curl.
> 

> [!NOTE] What is daemon off?
> Note: We use `CMD ["nginx", "-g", "daemon off;"]` because docker expects the container to run on the foreground, and the  `daemon off;` does that. If the main process within container exits, then container stops. 
> 

```bash
# removes locally installed image
docker rmi <repository_name:tag>
``` 
---
```bash
# exec into a running container
docker exec -it <container_name> /bin/sh
``` 

> [!NOTE] What Happens If Workdir Directory Does Not Exist?
> 
> **Note**: When we use `WORKDIR` directive, and if the following directory does not exist, docker creates it automatically.
> 

> [!NOTE] Where to Find Base Images?
> **Note**: Base images can be found from dockerhub. For instance:
> 	 python alpine: https://hub.docker.com/_/python/tags?page=&page_size=&ordering=&name=alpine

> [!NOTE] How to Make Dockerfile Ignore Files or Folders During Copy Directive?
> **Note**: For dockerfile to ignore some files or folders during copy process, we can create `.dockerignore` file and put the names in there.

> [!NOTE] What is the Difference Between RUN and CMD directives?
> The RUN directives are used to execute statements within the container filesystem to build and customize the container image, thus modifying the image layers. The idea of using a CMD command is to provide the default command(s) with the container image that will be executed at runtime.

> [!NOTE] What is the Difference Between ENTRYPOINT and CMD Directives?
> Every Docker container has a default `ENTRYPOINT – /bin/sh -c`. Anything you add to CMD is appended post-ENTRYPOINT and executed; for example, `CMD ["nginx", "-g", "daemon off;"]` will be generated as `/bin/sh -c nginx -g daemon off`. 

> [!NOTE] When to Use `CMD`; When to Use `ENTRYPOINT`?
> **Note**: Flexibility -> Use `CMD` when you want to provide default arguments to an entrypoint command but still allow the user to override it. Use `ENTRYPOINT` when you want to ensure a specific command is always executed. 
> ```bash
> FROM ubuntu
> ENTRYPOINT ["top", "-b"]
> CMD ["-c"]
> 
> # If we execute `docker run myubuntu` docker will execute `top -b -c`
> # If we execute `docker run my ubuntu -d 1`, docker will execute 'top -b -d 1'
> ```
> 

```bash
# Build the image in plain progress to see each step of creation
docker build --progress=plain -t <image_name:tag> .
```

> [!NOTE] Why we need privilege access to run `docker build` within a container?
> * **Docker Daemon Communication**: The `docker build` command interacts with the Docker daemon to perform the build process. To communicate with the Docker daemon, the container needs access to the Docker socket (`/var/run/docker.sock`), which typically requires elevated permissions.

---
```bash
# Delete all images with a single command
docker rmi $(docker images -q)
```
---
```bash
# Check the IP address of a container
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name_or_id>
```

---
```bash
# List all docker volumes
docker volume ls

# Check the mounting point of volume
docker volume inspect <volume_name> --format '{{ .Mountpoint }}'

# Explore volume contents (retrieved from previous step)
ls -l <mount_point>

# Delete a docker volume
docker volume rm <volume_name>
```
---
```bash
# List all image ids in the system
docker images -q

# Delete all images in system
docker rmi $(docker images -q)
```
