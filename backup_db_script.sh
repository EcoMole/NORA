#!/bin/bash

# Set the script to fail if any command fails
set -e

# need to specify the whole path because cron job runs in a different environment.
# When running through cron, the current directory is typically the home directory of
# the user who owns the cron job, not the directory where this script file and the .env file reside
source /opt/Nora/NORA/.env

DATE=$(date +'%Y-%m-%d_%H-%M-%S')
echo "$DATE   $DB_NAME - Creating backup"

DB_NAME=$DB_NAME
DB_USER=$DB_USER
DB_PASSWORD=$DB_PASSWORD
DB_HOST=$DB_HOST
DB_PORT=$DB_PORT
BACKUP_DIR=$BACKUP_DIR
BACKUP_RETENTION_DAYS=$BACKUP_RETENTION_DAYS

BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_backup_$DATE.sql"

# Create backup
PGPASSWORD=$DB_PASSWORD pg_dump -U $DB_USER -h $DB_HOST -p $DB_PORT $DB_NAME > $BACKUP_FILE

# Check if backup was successful
if [ $? -eq 0 ]; then
  echo "Backup successful: $BACKUP_FILE"
else
  echo "Backup failed"
fi
echo ""

# Remove backups older than 30 days
DATE=$(date +'%Y-%m-%d_%H-%M-%S')
echo "$DATE   Removing all .sql backups older than $BACKUP_RETENTION_DAYS days"

find $BACKUP_DIR -type f -mtime +$BACKUP_RETENTION_DAYS -name '*.sql' -exec rm {} \;

# Check if removal was successful
if [ $? -eq 0 ]; then
  echo "Removal without errors"
else
  echo "Removal failed"
fi
echo ""
