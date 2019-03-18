#coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect

import redis


app = Flask(__name__)

#配置信息
class Config(__name__):

    DEBUG = True
    SECRET_KEY = 'oneiiinstack'

    #数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/ihome'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    #flask-session
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_USE_SIGNER = True #对cookie中的sessionID进行隐藏
    PERMANENT_SESSION_LIFETIME = 86400 #session数据的有效期，秒数

app.config.from_object(Config)

#数据库
db = SQLAlchemy(app)

#创建redis连接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)

#利用flask-session，将session保存到redis中
Session(app)

#为flask补充csrf防护机制
CSRFProtect(app)

@app.route('index')
def index():

    return 'index page'

if __name__ == '__main__':
    app.run()