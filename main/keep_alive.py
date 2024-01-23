# random trash keep_alive script update this if you want to

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Fuck u my nigga"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()