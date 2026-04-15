#!/bin/bash

set -e

CLUSTER_NAME=$1
SERVICE_NAME=$2

echo "Updating ECS service..."

aws ecs update-service \
  --cluster $CLUSTER_NAME \
  --service $SERVICE_NAME \
  --force-new-deployment

echo "Deployment triggered!"