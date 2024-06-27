#!/bin/bash

# Load environment variables from .env file or environment
source .env

# Variables
DB_NAME=$DB_NAME
DB_USER=$DB_USER
DB_PORT=$DB_PORT
BACKUP_DIR=$BACKUP_DIR
DATE=$(date +'%Y-%m-%d_%H-%M-%S')
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_backup_$DATE.sql"

# Create backup
pg_dump -U $DB_USER -h $DB_HOST $DB_NAME > $BACKUP_FILE

# Optional: Remove backups older than 30 days
find $BACKUP_DIR -type f -mtime +30 -name '*.sql' -exec rm {} \;
