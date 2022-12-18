# 7/20 Docker & SHAP Writeup

## Summary
A Jupyter Tensorflow notebook image was built off of to generate a custom docker image. This custom image was modified to run an instance of the SHAP notebook, a notebook that creates small machine learning models based on the work of researcher Eduardo Lopez. This image can then be run to create a ready-to-use instance of the Jupyter Notebook. 

## Details
### Jupyter Docker Stacks
Jupyter has a collection of Docker images under the group name Jupyter Docker Stacks. [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/#) are ready-to-run and contain Jupyter applications such as Jupyter Server, Jupyter Notebooks, and Jupyter Lab. The Dockerfiles used to build the images are available via their [GitHub page](https://github.com/jupyter/docker-stacks). 

### Custom Docker Image
The custom Docker Image starts with a "base image" of Jupyter's Tensorflow image: 

```python
FROM jupyter/tensorflow-notebook:latest
```

From there, a Python 3.7 kernel is created using Python 3.7.13: 

```
ARG conda_env=python3713
ARG py_ver=3.7

RUN mamba create --quiet --yes -p "${CONDA_DIR}/envs/${conda_env}" python=${py_ver} ipython ipykernel && \
    mamba clean --all -f -y

RUN "${CONDA_DIR}/envs/${conda_env}/bin/python" -m ipykernel install --user --name="${conda_env}" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
```

Finally, the pre-existing SHAP notebook and corresponding data is added to the notebook: 

```
RUN mkdir /home/jovyan/notebooks/
RUN mkdir /home/jovyan/data/
RUN mkdir /home/jovyan/external/


COPY ./Notebooks/ /home/jovyan/notebooks/
COPY ./Data/ /home/jovyan/data/
```

### Building and Running the Image

From there, the image and container are built in the usual Docker process: 

```
docker build -t <name of image> .
docker run -p 8888:8888 <name of image>
```

After the ```run``` command is issued, a URL is printed in the terminal. This URL can be used to access the Jupyter Server instance in the container. From there, the SHAP notebook can be found under the ```notebook``` folder. The notebook can be run like any other notebook. 