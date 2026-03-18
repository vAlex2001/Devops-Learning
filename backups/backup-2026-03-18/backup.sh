#!/bin/bash

# Backup script
# Creates a dated backup of the scripts folder

# Variables
SOURCE=~/devops-journey/scripts
BACKUP_DIR=~/devops-journey/backups
DATE=$(date +%Y-%m-%d)
BACKUP_NAME="backup-$DATE"
LOG_FILE=~/devops-journey/backup.log

# Creates backup folder if not existent
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Creating backup directory..."
    mkdir $BACKUP_DIR
fi

# Check if today's backup already exists"
if [ -d "$BACKUP_DIR/$BACKUP_NAME"]; then
    echo "Backup for $DATE already exists. Skipping."
    echo "$(date): Backup skipped - already exists" >> $LOG_FILE
    exit 0
fi

# Creates the backup
echo "Starting backup..."
cp -r $SOURCE $BACKUP_DIR/$BACKUP_NAME

# Verify backup was created successfully
if [ -d $BACKUP_DIR/$BACKUP_NAME ]; then
    echo "Backup completed successfully."
    echo "Location: $BACKUP_DIR/$BACKUP_NAME"
    echo "Files backed up:"
    for FILE in $BACKUP_DIR/$BACKUP_NAME/*.sh; do
        echo " - $FILE"
    done
    echo "$(date): Backup successful - $BACKUP_NAME" >> $LOG_FILE
else
    echo "Backup failed."
    echo "$(date): Backup FAILED" >> $LOG_FILE
    exit 1
fi