
# Memo System Install README

This document explains how to install and run the Memo System application on your machine.

## Prerequisites

-   Docker installed on your machine.
-   Git installed on your machine.

## Installation

1.  Clone the Memo System repository from Github.
 
    `git clone https://github.com/plaris-solar/memosystem.git` 
    
2.  Navigate into the cloned repository.
        
    `cd memosystem` 
    
3.  Create the directory for storing memos and memo meta data.
        
    mkdir memo_files
    mkdir memo_files/static
    mkdir memo_files/mysql
    mkdir memo_files/sqlite
    
4.  Copy `/memosystem/memos/settings_local.py` to the new `config` directory.
    
    `cp /memosystem/memos/settings_local.py /memo_files/static/config/settings_local.py` 
    
5.  Navigate to the root of the project.
    
    bashCopy code
    
    `cd ..` 
    
6.  Run the following command to build and start the containers:
    
    `docker-compose up -d` 
    
7.  Verify that the containers are running with the following command:
    
    `docker-compose ps` 
    
    This should show a list of running containers including `memosystem` and `mysql`.
    
8.  Once the containers are up and running, create the database tables by running the following command:
 
    `cat /memosystem/memos/db_dump.sql | docker exec -i mysql /usr/bin/mysql -u root --password=test123 memos` 
    
9.  Access the Memo System application by navigating to `http://localhost` in your web browser.
    

## Notes

-   When the system is running it will need to store the memos and memo meta data onto a permanent file system on the host. The docker compose will need to "mount" the local file system into the docker containers. In my installation I created a directory at the top level called "memo_files". In this directory, I make three subdirectories, one for the files (static), one for the MySQL, and one for the SQLite. You should create these directories and update the `docker-compose.yml` file with the correct paths to these directories on your machine.
    
-   The `docker-compose.yml` paths need to be adapted to the local filesystem. The current paths are set up for the author's local file system.
    
-   If you encounter any issues, please refer to the official Docker and Docker Compose documentation.