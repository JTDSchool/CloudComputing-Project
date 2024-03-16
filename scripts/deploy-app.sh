#!/bin/bash

set -e
cd app

export PROJECT_ID="cloudcomputing-project-416904"
export PROJECT_NAME="cloudcomputing-project"

export REPOSITORY_NAME="text-summerization"
export REPOSITORY_FORMAT="docker"

export IMAGE="text-summerization-app"

export LOCATION="us-east4"
export TAG="v1"

docker build -t $LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/$IMAGE:$TAG . --platform linux/amd64

docker push $LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/$IMAGE:$TAG

gcloud run deploy "text-summarization-app" \
    --image=$LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/$IMAGE:$TAG --platform managed --allow-unauthenticated
