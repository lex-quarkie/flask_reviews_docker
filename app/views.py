from app.app import app

import socket

@app.route("/")
def hello():
    return "Hello Container World! My hostname is %s.\n" % (socket.gethostname())
