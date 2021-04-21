import time
import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  ENV = os.getenv('ENV')
  return 'Hello ECS!'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
