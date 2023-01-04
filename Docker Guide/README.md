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
docker run postgres:14
```
The above command will run the `latest postgres image`. *postgres* is the image name. If you want to run a specific version of the image, you have to specify as so called *`tag`*.

**Important options:**
- **`-it`**: This instructs docker to allocate a pseudo.TTY connected to the container's stdin; creating an interactive *bash* shell in the container.
- **`-e ENVIRONMENT_VAR=VALUE`**: Some images need environment variables which help to run the image properly. E.g., to run postgres properly, you have to set password by `POSTGRES_PASSWORD=mysecretpassword`.
- **`-d`**: Detach mode. When you run the image, it keeps your terminal busy. You can enter or command any other command or have to keep open the termina to run the image continuously. If you pass this option, then the terminal will be detached and you can work with it.
- **`--name some-name`**: If you dont specify this option, docker comes up a name on its own and sometimes it is confisuing. For that, you can name the container. You can't name same twice or without deleting the previous container.
