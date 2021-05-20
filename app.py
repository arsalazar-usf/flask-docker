import time
import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  ENV = os.getenv('ENV')
  return f'Hello {ENV}!'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
