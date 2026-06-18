import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

r.set('test_key', 'hello from python', ex=10)  # expires in 10 seconds
print(r.get('test_key'))