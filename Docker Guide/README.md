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

When you don't mention the tag, this command will pull the latest image. If you want to pull postgres image version 14, then the command will be

```bash
docker pull postgres:14
```

*Note: `:14` is called `tag`.*

### [`docker image`](https://docs.docker.com/engine/reference/commandline/image):

- Using this command, you can see list of images are there in your local machine. This command gives you some information about the docker images.
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
- **`-d`**: Detach mode. When you run the image, it keeps your terminal busy. You can enter or command any other command or have to keep open the terminal to run the image continuously. If you pass this option, then the terminal will be detached and you can work with it.
- **`--name some-name`**: If you don't specify this option, docker comes up a name on its own and sometimes it is confusing. For that, you can name the container. You can't name same twice or without deleting the previous container.
- **`-p host_port:container_port`**: Some docker image(s) you run together. But it is possible that the port is same and that can conflict to your application. For that, you can open a port (host_port) to your local machine that will communicate with the container_port. Very important option. To know which port the container is using, you can use `docker ps` command. This concept is known as *`port mapping`*.
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

### [`docker container ls`](https://docs.docker.com/engine/reference/commandline/container_ls):
An alternative of the command `docker ps` to list out all the active docker containers.

```bash
docker container ls
```

If you want all the containers whatever it is running or not, command this:
```bash
docker container ls -a
```

### [`docker container prune`](https://docs.docker.com/engine/reference/commandline/container_prune/):

Remove all the stopped containers from your local machine. This is a very **dangerous command.** You have to be very careful when you are using it. Though it does remove the stopped containers but does not remove the volumes associated with the containers.

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

### Connect docker [mongo-express](https://hub.docker.com/_/mongo-express) with [mongodb](https://hub.docker.com/_/mongo) | [Docker Compose](https://docs.docker.com/compose/reference):
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
Now the web app of mongodb-express container is running and you can visit by using the browser. The url is http://localhost:8081. You can visit it. If we stop the `mongodb` container that we have created, it will also stop the `mongo-express` container because `mongodb` container is the dependency of the `mongo-express` container.

So, we have wrote lots of long commands to do this. This can cause issue if you have done a small spelling mistake. To solve this issue, [`docker compose`](https://docs.docker.com/compose/reference) come out. For this you can create a yml file. The file name can be anything. For our case, we can name it as *docker-compose.yml*.

```yml
version: '3'
services:
    mongodb:
        image: mongo
        ports:
            - "27017:27017"
        environment:
            - MONGO_INITDB_ROOT_USERNAME=admin
            - MONGO_INITDB_ROOT_PASSWORD=password
        volumes:
            - mymongo-data:/data/db
    mongo-express:
        image: mongo-express
        restart: always
        ports:
            - "8081:8081"
        environment:
            - ME_CONFIG_MONGODB_SERVER=mongodb
            - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
            - ME_CONFIG_MONGODB_ADMINPASSWORD=password
volumes:
    mymongo-data:
        driver: local
```
After creating the compose yml file, you can run the file by the following command:

```bash
docker-compose -f docker-compose.yml up
```

The best thing with docker compose is that it will create a network by-default and will put all the containers into it. We don't have to specify separately in the docker compose file. Check out the `mongodb` container. One option is `volumes`. That is different with the lowers `volumes` settings. The value of`volumes` of `mongodb` container should be default value of the mongo image. That can be different with MySQL or any other image. For that, you have to look to the documentation of the images. By using the `volumes`, you can detach and attach the volume(s) with the container according to the requirements.

To stop this compose, you can run the command to a another terminal. This will also remove the containers from your local machine automatically. You don't have to do it manually.

```bash
docker-compose -f docker-compose.yml down
```

### Flask APP | Create Docker Image | Push Image to Docker Hub:

To create an docker image, you have to create a file named `Dockerfile` inside your root project directory. According to the demo-flask app, add the below commands to the `Dockerfile`.

```Dockerfile
# define the base image
FROM python:3-alpine3.15
# define the working directory
WORKDIR /app
# copy everything and move those to the directory
COPY . /app
# install the required python packages using pip
RUN pip install -r requirements.txt
# expose the port in which this application will run.
# This is defined to the python flask file.
EXPOSE 3000
# Now start the application, the entry point of your app
CMD python ./index.py
```

Now to build the image of your flask app, you can run the below command. `sayanroy7` is the username of mine (to get your username, you have to create an account to [docker hub](https://hub.docker.com)). `flask-docker-demo` is the image of the image that you are giving. `:0.0.1.RELEASE` is the `flag` of this image.

```bash
docker build -t sayanroy7/flask-docker-demo:0.0.1.RELEASE .
```

After building the image, you can see it to your Docker Desktop app. Before pushing to the hub, check that is it working fine or not. For that, run the simple command:

```bash
docker container run -d -p 3000:3000 --name flask-docker-demo sayanroy7/flask-docker-demo:0.0.1.RELEASE
```

If you go to the browser and hit http://localhost:3000, you should get the result as

```bash
{"message":"Hey there Python"}
```

If the image is working fine, then push the image to the Docker Hub by the command. If you already signed in to your Docker Desktop, then the image will be uploaded smoothly otherwise it will prompt for the authentications.

```bash
docker push sayanroy7/flask-docker-demo:0.0.1.RELEASE 
```

And in your Docker Hub, you can see the image under the *Repositories* tab!! 