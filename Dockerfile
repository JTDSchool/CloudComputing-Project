FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP app.py

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

# Make port 8888 available to the world outside this container for JupyterLab
# Make port 5000 available for Flask
EXPOSE 8888 8080

RUN pip install jupyterlab
RUN pip install ipywidgets

# Run JupyterLab and Flask app
CMD ["sh", "-c", "jupyter lab --ip='*' --port=8888 --no-browser --allow-root & flask run --host=0.0.0.0 --port=8080"]
