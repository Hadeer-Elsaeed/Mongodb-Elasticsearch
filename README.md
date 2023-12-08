# Mongodb-Elasticsearch

This project is a simple demonstration of synchronizing MongoDB and Elasticsearch using Logstash. It includes a Docker Compose file for setting up containers for MongoDB, Logstash, Elasticsearch, and a sample Python application.


## Prerequisites
Docker installed on your machine.

## Getting Started
1- clone the repository

    git clone git@github.com:Hadeer-Elsaeed/Mongodb-Elasticsearch.git 

2- Navigate to the project directory

    cd Mongodb-Elasticsearch

3- Start the Docker containers

    docker compose up -d 

4- when the container app is up and started adding data in Mongodb, Logstash will automatically pick up the changes and index the data into Elasticsearch.

## Folder Structure
  - app: contains the Python application for inserting data into MongoDB.
  - logstash: Contains Logstash configurations for connecting MongoDB and Elasticsearch.
  - docker-compose.yml: Docker Compose file to orchestrate the containers.

