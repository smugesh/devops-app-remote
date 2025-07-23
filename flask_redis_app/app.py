from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = os.getenv('REDIS_PORT', '6379')
redis_db = os.getenv('REDIS_DB', '0')

redis_client = Redis(host=redis_host, port=int(redis_port), db=int(redis_db))

@app.route('/')
def hello():
    count = redis_client.incr('visits')
    return f'Hello from Flask! Thos page has been visited {count} times. \n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)