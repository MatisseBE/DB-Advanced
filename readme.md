# DB Advanced
## Linux

### Install Python

In your Ubuntu terminal execute the following commands:

`sudo apt update`

`sudo apt -y upgrade`

`sudo apt install python3.9`

`sudo apt install -y python3-pip`

`pip3 install bs4`

`pip3 install pandas`

`pip3 install pymongo`

`pip3 install redis`

Navigate to the folder in which you have saved the scraper using the 'cd' command and execute the following code:

`python3 bitcoinminer.py`

Then, for each update, execute: 

`python3 contactredis.py`


## Install MongoDB
`wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -`

`echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list`

`sudo apt-get update`

`sudo apt-get install -y mongodb-org`

`ps --no-headers -o comm 1`

## Start MongoDB
`sudo systemctl start mongod`

`sudo systemctl daemon-reload`

`sudo systemctl status mongod` (should show running)

`sudo systemctl enable mongod`

`sudo systemctl stop mongod`

`sudo systemctl restart mongod`

`mongo` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(to start using it)


## MongoDB compass
`wget https://downloads.mongodb.com/compass/mongodb-compass_1.25.0_amd64.deb`

`sudo dpkg -i mongodb-compass_1.25.0_amd64.deb`

`mongodb-compass`

## Install Redis
`wget http://download.redis.io/redis-stable.tar.gz`
`tar xvzf redis-stable.tar.gz`
`cd redis-stable`
`make`

# Install Docker
`https://www.docker.com/get-started`

Download any additional software if prompted.

`docker run hello-world`

`docker pull mongo`

`docker pull redis`



# Run the program
`docker run -p 8080:6379 redis`

`docker run -p 8081:27017 mongo`

run `bitcoinminer.py`
then `contactredis.py`


# DB Advanced
## Prerequisites
### Install Docker
`https://www.docker.com/get-started`

Download any additional software if prompted.

`docker pull mongo`

`docker pull redis`

### Install MongoDB Compass
Download the latest MongoDB compass for your platform via the following link:

`https://www.mongodb.com/products/compass` 


## Get started
Clone this repository

Start Docker Desktop, make sure it say "Running" at the bottom left.

Execute the .bat files in order, on you Windows machine.

Start MongoDB compass to see entries added to the database.

In Compass, click `Fill in connection fields individually`

Set hostname `localhost`
Set port `8080`

## What's happening?
The .bat file will start Redis and MongoDB in a Docker Container.  

Once these containers are booted, our script will run. Every minute you'll see a line with the hashcode of the biggest bitcointransaction of last minute. 



