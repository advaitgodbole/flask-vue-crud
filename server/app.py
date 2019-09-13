from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS (Cross Origin Routing Sharing)
# Why do we need Flask-CORS? In order to make cross-origin requests -- e.g., 
# requests that originate from a different protocol, IP address, domain name, 
# or port -- you need to enable Cross Origin Resource Sharing (CORS). 
# Flask-CORS handles this for us.

CORS(app,resources={r'/*':{'origins':'*'}})


# sanity check route
@app.route('/ping',methods=['GET'])
def ping_pong():
    return jsonify('pong')


if __name__ == '__main__':
    app.run()
