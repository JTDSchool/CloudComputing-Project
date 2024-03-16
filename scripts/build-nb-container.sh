#!/bin/bash

docker stop text-summerization-notebooks
docker rm text-summerization-notebooks

set -e

docker build -t text-summerization-notebooks ./app/model/
docker run -d --name text-summerization-notebooks --mount type=bind,source="$(pwd)/app/model",target=/notebooks -p 8888:8888 text-summerization-notebooks

docker logs text-summerization-notebooks
