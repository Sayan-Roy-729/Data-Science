# [Docker Guide](https://docs.docker.com)

## What is Docker Image & Docker Container?

Docker Image is an executable package of software that includes everything needed to run an application. This image informs how a container should instantiate, determining which software components will run and how. Docker Container is a virtual environment that bundles application code with all the dependencies required to run the application. The application runs quickly and reliably from one computing environment to another. One Docker Container only can hold one Docker Image.

You can find the images from [Docker Hub](https://hub.docker.com/search).

## [Reference of Docker | Some Important Commands](https://docs.docker.com/reference)

### [Check the version](https://docs.docker.com/engine/reference/commandline/version):

There are 2 commands that can help to check the docker version
```bash
docker version
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
