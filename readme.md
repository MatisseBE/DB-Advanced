# DB Advanced
## What is this
This repository is created as an assignment for Thomas More University.

It will scrape a website to find the largest transaction made in Bitcoin for any minute. This entry will be added to a MongoDB, set-up in a docker container. Redis is used to store a pandas data frame with all scraped data of the last minute. Redis also runs in Docker 
## Prerequisites
### Install Docker
`https://www.docker.com/get-started`

Download any additional software if prompted.

`docker pull mongo`

`docker pull redis`

### Install MongoDB Compass
Download the latest MongoDB compass for your platform via the following link:

`https://www.mongodb.com/products/compass` 

### Install Python 3.9
Install python 3.9 (including pip) and run the following commands:

`pip3 install bs4`

`pip3 install pandas`

`pip3 install pymongo`

`pip3 install redis`

## Get started
Clone this repository

Start Docker Desktop, make sure it say "Running" at the bottom left.

Execute the .bat files in order, on you Windows machine. Make sure you leave the prompted windows open.

Start MongoDB compass to see entries added to the database.

In Compass, click `Fill in connection fields individually`

Set hostname `localhost`
and set port `8081` then click `Connect`

Navigate `Mining_operation < Largest_entry`

## What's happening?
The .bat files will start Redis and MongoDB in a Docker Container.

Once these containers are booted, our script will run. Every minute you'll see a line with the hashcode of the biggest bitcointransaction of last minute. 

In MongoDB you can see these entries added with more information. Make sure you click refresh periodically.



