import redis
#host name when using a bridge docker network driver can use just the name of another container running on the same bridge network
r = redis.Redis(host='redis-stack', port=6379, db=0)

r.set('foo', 'bar')

r.set('fire', 'burning')
r.set('air', 'blowing')
r.set('earth', 'rotating')
r.set('water', 'flowing')

var = 'growing'
r.set('plant', f'{var}')

print (r.get('foo'))

r.set('foo', 'zebra')

print(r.get('foo'))

#in docker swarm if your container exits it is considered a fail so in order to address this I added a do nothing loop
while(True):
    pass
