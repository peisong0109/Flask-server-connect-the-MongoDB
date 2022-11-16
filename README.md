# Flask-server-connect-the-MongoDB

Docker based Flask server connect another Docker based MongoDB

### Deployment of MongoDB:

    docker run --name mongodb -d -p 27017:27017 mongo

### Connect MongoDB database from another docker container:

    client = pymongo.MongoClient(host='mongodb://47.243.109.255', port=27017)
Here we must use the specific IP of the cloud server. 
Do not use: localhost, 127.0.0.1, or 0.0.0.0. 
