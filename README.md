# CSCI 4905/6905 Intelligent Systems Visualization Container Project
This repository houses the files and instructions for the CSCI 4905/6905 Intelligent Systems Spring 2023 project. 


## Various tasks associated with creating Docker images and containers:

### Build the image 
```
docker build <directory with the dockerfile>
```

### Create the container
There are multiple ways to create and rumdd.yoda@gmail.com n a container, below are two of the available options:

#### Create a version of the container that is mounted to your host machine
Generally, you want a Docker container to run in a (mostly) isolated manner. It should have all the data it needs to run the containerized application or it should have some process to obtain the information it needs (say an API call). The container is generally not supposed to read/write on the host operating system. So why would we want to mount a volume to the host operating system? When a Docker container is destroyed, all of the contains of the container are also destroyed with '''no way to recover them'''.  This is okay when we have a base image where all of the details on what goes in the container are stored there, but for this project you will be developing a notebook within the container. This means that if 1. you do not mount a volume on the host machine and 2. you do not modify your file on that volume, '''you will lose all your work on your container if the container is destroyed'''. 

```
docker run -d --mount type=bind,source="<absolute path where the project folder is stored>\Notebooks",target=/home/jovyan/notebooks -p 8888:8888 <image name>
```

#### Create a completely isolated version of the container
This is the way the container should be run once the project is completed, all of the necessary files to run the image and the notebook will be stored within the container itself. This is '''NOT''' the preferred way for you to do your development work. '''You should only run a container for this project in this manner when you are finished doing development within the container and your notebook has been saved on your host machine.'''

```
docker run -d -p 8888:8888 <image name>
```

### Obtaining the Jupyter Notebooks key from a running container

<!---   TODO: Write instructions for building the container and having a volume mounted in this folder
        TODO: Decide on and add a dataset to the Data folder
 -->

### Stopping Containers

### Removing Containers

### Deleting Images
