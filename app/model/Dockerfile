FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /notebooks
COPY . /notebooks

# Make port 8888 available to the world outside this container for JupyterLab
EXPOSE 8888 

RUN pip install jupyterlab
RUN pip install ipywidgets

# Run JupyterLab and Flask app
CMD ["sh", "-c", "jupyter lab --ip='*' --port=8888 --no-browser --allow-root"]
