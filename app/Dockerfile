FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP app.py

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Make port 8080 available for Flask
EXPOSE 8080

# Run JupyterLab and Flask app
CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=8080"]
