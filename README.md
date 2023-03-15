# CSCI 4905/6905 Intelligent Systems Visualization Container Project
This repository houses the files and instructions for the CSCI 4905/6905 Intelligent Systems Spring 2023 project.   


## Various tasks associated with creating Docker images and containers:

### Adding your own data to the Notebook
Simply place an unzipped version of your data within the Data directory of this repository. When you build the image (using the instructions below), it will automatically pull in the data at creation time.

### Build the Image 
```
docker build -t example/intelsystimage <directory with the dockerfile>
```

Note that you can change the name of the image something other than example/intelsystimage, but all instructions below will assume that is the name of the image  


### Create and Run the container
There are multiple ways to create and run a container, below are two of the available options:  

#### Create a version of the container that is mounted to your host machine
Generally, you want a Docker container to run in a (mostly) isolated manner. It should have all the data it needs to run the containerized application or it should have some process to obtain the information it needs (say an API call). The container is generally not supposed to read/write on the host operating system. So why would we want to mount a volume to the host operating system? When a Docker container is destroyed, all of the contains of the container are also destroyed with **no way to recover them**.  This is okay when we have a base image where all of the details on what goes in the container are stored there, but for this project you will be developing a notebook within the container. This means that if 1. you do not mount a volume on the host machine and 2. you do not modify your file on that volume, **you will lose all your work on your container if the container is destroyed**. 

```
docker run -d --name JupyterNotebookContainer --mount type=bind,source="<absolute path where the project folder is stored>\Notebooks",target=/home/jovyan/notebooks -p 8888:8888 example/intelsystimage
```

If you are using macOS, make sure to use / instead of \

```
docker run -d --name JupyterNotebookContainer --mount type=bind,source="<absolute path where the project folder is stored>/Notebooks",target=/home/jovyan/notebooks -p 8888:8888 example/intelsystimage
```

Note that you can change the name of the container to something other than JupyterNotebookContainer, but all instructions below will assume that is the name of the container.   

#### Create a completely isolated version of the container
This is the way the container should be run once the project is completed, all of the necessary files to run the image and the notebook will be stored within the container itself. This is **NOT** the preferred way for you to do your development work. **You should only run a container for this project in this manner when you are finished doing development within the container and your notebook has been saved on your host machine.**

```
docker run -d --name JupyterNotebookContainer  -p 8888:8888 example/intelsystimage
```  

### Accessing the Jupyter Notebook within the container

```bash
docker log JupyterNotebookContainer 
```

If everything is working as expected, the output should look like the following: 

```bash
Entered start.sh with args: jupyter lab
Executing the command: jupyter lab
[I 2023-02-15 03:11:15.424 ServerApp] jupyterlab | extension was successfully linked.
[I 2023-02-15 03:11:15.432 ServerApp] nbclassic | extension was successfully linked.
[I 2023-02-15 03:11:15.434 ServerApp] Writing Jupyter server cookie secret to /home/jovyan/.local/share/jupyter/runtime/jupyter_cookie_secret
[I 2023-02-15 03:11:15.716 ServerApp] notebook_shim | extension was successfully linked.
[I 2023-02-15 03:11:15.737 ServerApp] notebook_shim | extension was successfully loaded.
[I 2023-02-15 03:11:15.738 LabApp] JupyterLab extension loaded from /opt/conda/lib/python3.10/site-packages/jupyterlab
[I 2023-02-15 03:11:15.738 LabApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
[I 2023-02-15 03:11:15.741 ServerApp] jupyterlab | extension was successfully loaded.
[I 2023-02-15 03:11:15.746 ServerApp] nbclassic | extension was successfully loaded.
[I 2023-02-15 03:11:15.747 ServerApp] Serving notebooks from local directory: /home/jovyan
[I 2023-02-15 03:11:15.747 ServerApp] Jupyter Server 1.18.1 is running at:
[I 2023-02-15 03:11:15.747 ServerApp] http://dad3dd418f12:8888/lab?token=4c288646efffc5ec6f34cfc8ebd41e583ae6f157fe4f85d5
[I 2023-02-15 03:11:15.747 ServerApp]  or http://127.0.0.1:8888/lab?token=4c288646efffc5ec6f34cfc8ebd41e583ae6f157fe4f85d5
[I 2023-02-15 03:11:15.747 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2023-02-15 03:11:15.749 ServerApp]

    To access the server, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/jpserver-7-open.html
    Or copy and paste one of these URLs:
        http://dad3dd418f12:8888/lab?token=4c288646efffc5ec6f34cfc8ebd41e583ae6f157fe4f85d5
     or http://127.0.0.1:8888/lab?token=4c288646efffc5ec6f34cfc8ebd41e583ae6f157fe4f85d5
```

Copy and paste one of the two URLs at the bottom of the output into a web browser.   


### Starting the Container 
The ```docker run``` command above will create and start the container, but if the container is stopped (say because of a system restart), you can restart the container like so:
```bash
docker start JupyterNotebookContainer
```  


### Stopping the Container
```bash
docker stop JupyterNotebookContainer
```  


### Removing the Container
```bash
docker rm JupyterNotebookContainer
```  


### Deleting the Image
```bash
docker image rm example/intelsystimage
```  

## Additional Documentation
- [Docker CLI documentation](https://docs.docker.com/engine/reference/commandline/cli/)
- [Jupyter Notebook Documentation](https://docs.jupyter.org/en/latest/)
