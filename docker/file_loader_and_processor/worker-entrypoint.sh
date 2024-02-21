#!/bin/sh

until cd /app/file_loader_and_processor
do
    echo "Waiting for server volume..."
done

celery -A file_loader_and_processor worker --loglevel=info --concurrency 1 -E
