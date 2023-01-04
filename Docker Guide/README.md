# [Docker Guide](https://docs.docker.com)

## What is Docker Image & Docker Container?

Docker Image is an executable package of software that includes everything needed to run an application. This image informs how a container should instantiate, determining which software components will run and how. Docker Container is a virtual environment that bundles application code with all the dependencies required to run the application. The application runs quickly and reliably from one computing environment to another. One Docker Container only can hold one Docker Image.

You can find the images from [Docker Hub](https://hub.docker.com/search).

## [Reference of Docker | Some Important Commands](https://docs.docker.com/reference)

### [Check the version](https://docs.docker.com/engine/reference/commandline/version):

There are 2 commands that can help to check the docker version
```bash
docker version
```
or
```bash
docker -v
```

### [`docker pull`](https://docs.docker.com/engine/reference/commandline/pull):

Pull an image or a repository from a registry/docker hub. Like to use [postgres](https://hub.docker.com/_/postgres), you have to pull that image first by the below command:

```bash
docker pull postgres
```

When you dont mention the tag, this command will pull the latest image. If you want to pull postgres image version 14, then the command will be

```bash
docker pull postgres:14
```

*Note: `:14` is called `tag`.*

### [`docker image`](https://docs.docker.com/engine/reference/commandline/image):

- Using this commnand, you can see list of images are there in your local machine. This command gives you some information about the docker images.
```bash
docker image ls
```

### [`docker ps`](https://docs.docker.com/engine/reference/commandline/ps):

Same as `docker image` command, this command helps to work with containers. For example, to list down all the containers of your local machine, this below command is used.
```bash
docker ps
```

### [`docker run`](https://docs.docker.com/engine/reference/commandline/run):

One of the most used command in docker family. It helps to run the image that you have pulled or have created to your local machine. E.g.,

```bash
docker run postgres
```
or
```bash
docker run postgres:13.8
```
The above command will run the `latest postgres image`. *postgres* is the image name. If you want to run a specific version of the image, you have to specify as so called *`tag`*.

**Important options:**
- **`-it`**: This instructs docker to allocate a pseudo.TTY connected to the container's stdin; creating an interactive *bash* shell in the container.
- **`-e ENVIRONMENT_VAR=VALUE`**: Some images need environment variables which help to run the image properly. E.g., to run postgres properly, you have to set password by `POSTGRES_PASSWORD=mysecretpassword`.
- **`-d`**: Detach mode. When you run the image, it keeps your terminal busy. You can enter or command any other command or have to keep open the termina to run the image continuously. If you pass this option, then the terminal will be detached and you can work with it.
- **`--name some-name`**: If you dont specify this option, docker comes up a name on its own and sometimes it is confisuing. For that, you can name the container. You can't name same twice or without deleting the previous container.
- **`-p host_port:container_port`**: Some docker image(s) you run together. But it is possible that the port is same and that can conflict to your application. For that, you can open a port (host_port) to your local machine that will communicate with the container_port. Very important option. To know which port the container is using, you can use `docker ps` command. This concept is known as *`port maping`*.
- - **`--net network-name`**: Connect the container to a network. This can help to connect other containers with this containers easily. Otherwise different networks can't connect each other.

### [`docker stop`](https://docs.docker.com/engine/reference/commandline/stop) or [`docker container stop`](https://docs.docker.com/engine/reference/commandline/container_stop):

Stop one or more running containers.

```bash
docker stop container_name
or
docker stop container_id
or
docker container stop container_name
or
docker container stop container_id
```

### [`docker contailer ls`](https://docs.docker.com/engine/reference/commandline/container_ls):
An alternative of the command `docker ps` to list out all the active docker containers.

```bash
docker container ls
```

If you want all the containers whatever it is running or not, command this:
```bash
docker container ls -a
```

### [`docker container prune`](https://docs.docker.com/engine/reference/commandline/container_prune/):

Remove all the stopped containers from your local machine. This is a very **dangerous command.** You have to be very careful when you are using it. Though it does remove the stopped containes but does not remove the volumes associated with the containers.

```bash
docker container prune
```

### [`docker logs`](https://docs.docker.com/engine/reference/commandline/logs):

You can see the logs of the containers. It helps to get inside what is executing in containers.

```bash
docker logs container_name
or
docker logs container_id
```
## Docker Example:

### Connect docker [mongo-express](https://hub.docker.com/_/mongo-express) with [mondodb](https://hub.docker.com/_/mongo):
[MongoDB](https://hub.docker.com/_/mongo) is the database and the [MongoDB-Express](https://hub.docker.com/_/mongo-express) is the Web-based MongoDB admin interface, written with Node.js and express. So, we will start the container first of the MongoDB and then also start the MongoDB-Express container by connecting with the MongoDB network.

Create a network that both containers will connect together.
```bash
docker network create mongo-network
```

Start the MongoDB container:
```bash
docker run -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password --name mongodb --net mongo-network -d mongo
```

Now start the MongoDB-Express container:
```bash
docker run --network mongo-network -e ME_CONFIG_MONGODB_SERVER=mongodb -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin -e ME_CONFIG_MONGODB_ADMINPASSWORD=password -p 8081:8081 -d --name mongo-express mongo-express
```
