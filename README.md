First we will pull down the redis database server from docker hub. We will be using the redis/redis-stack image because we want the frontend database insights page available to us so we can see the effect our code has on the database.<br>
`docker pull redis/redis-stack`

Since we have both the redis database container running and our own client container running we need to set up docker networks to allow them to interact with each other.<br>
`docker network ls` lists the available networks by default you should have bridge host and none. Docker has 3 network drivers bridge host and null.The bridge network driver is used to connect multiple containers, the host network driver is used to forward the containers traffic to its host device, and the null network driver is used to completely isolate a container. There are more drivers to learn more you can read this https://docs.docker.com/engine/network/drivers/ . 

Next we will use this to create our bridge network that we will use to connect our redis client and redis database.<br>
`docker network create -d bridge redis-net`

Now we just need to run the docker containers specifying them to be on the same network.<br>
`docker run -d --network=redis-net --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest`

Before we run the redis client lets make sure that our redis insights page is up and running.
http://localhost:8001/

Now build and run our Redis client<br>
`docker build -t redis-test-client:1.0.0 .`<br>
 `docker run --name redis-test-client --network=redis-net redis-test-client:1.0.0`

Reload your redis insights page and data should now be visible.<br>

Examine the code and the python files in the redis test client code.