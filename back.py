from flask import Flask
from flask import request
from threading import Thread
import time
import requests

app = Flask('')


@app.route('/')
def home():
  return "I'm alive"


def run():
  app.run(host='0.0.0.0', port=80)


def keep_alive():
  t = Thread(target=run)
  t.start()

"""Вебхук, який не дає нашому боту впасти. Більш детально про це можете
ознайомитися тут: https://youtu.be/7mMrDIZWfcA?si=trRneW2DjlNuG-XL"""