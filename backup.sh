#!/bin/bash

# Export env vars
source .env.prod

echo "Creating database backup from MySQL server "$MYSQL_HOST

DATE=$(date +'%d-%m-%Y')
FILENAME="backup_nolla_$DATE.sql"
BACKUP_DIR=db_dumps/

echo "Creating file "$BACKUP_DIR$FILENAME

mysqldump --column-statistics=0 -h $MYSQL_HOST -P $MYSQL_PORT --user $MYSQL_USER --password --databases $MYSQL_DB > $BACKUP_DIR$FILENAME; 

echo "Finished creating database backup"
