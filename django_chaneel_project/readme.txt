=>Redis is very fast than other server .
1.pip3 install channels ->(https://redis.io/download)
$ wget https://download.redis.io/releases/redis-6.2.6.tar.gz
$ tar xzf redis-6.2.6.tar.gz
$ cd redis-6.2.6
$ make
The binaries that are now compiled are available in the src directory. Run Redis with:

$ src/redis-server
You can interact with Redis using the built-in client:

$ src/redis-cli
redis> set foo bar
OK
redis> get foo
"bar"
2.then install channes-redis 
3.register channels in installed app 
4.CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.pubsub.RedisPubSubChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}
=>https://pypi.org/project/channels-redis/
5.replace wsgi with this ASGI_APPLICATION = 'django_chaneel_project.asgi.application'
=>wsgi cannot support web-socket so we use asgi which easily can
=>ASGI->Asynchronous Server Gateway Interface
=>group name->broadcast
=>room name -> between two user
=> For testing -> https://websocketking.com/
=>url -> ws://127.0.0.1:8000/ws/ac/ for async


