# Instructions

## Build Image and Container

1. `docker build -t text-summerization-app .`
2. `docker run -d --name text-summerization-app --mount type=bind,source="$(pwd)",target=/app -p 8888:8888 -p 5001:5000 text-summarization-app`

This builds an image called text-summerization-app and uses that to create a container, exposing ports 8888 and 5000 (mapped to port 5001).

use `docker logs text-summerization-app` to get the link for the notebook, and go to `127.0.0.1:5001` to access the flask webapp.

-   `docker stop text-summerization-app` to stop the container
-   `docker start text-summerization-app` to start the app again
