from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from util import generate_key,hash_pass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mbdask1013@localhost/stackedCash'
db = SQLAlchemy(app)

class User(db.Model):
    pk = db.Column(db.Integer,primary_key = True)
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    email = db.Column(db.String(20),unique=True)
    password = db.Column(db.String(230),unique=True)
    token = db.Column(db.String(20),unique=True)


def __init__(self,firstname,lastname,email,password,token=''):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.password = hash_pass(password)
    self.token = token

@app.route('/post_user/<firstname>/<lastname>/<email>/<password>', methods = ['POST'])
def post_user(firstname,lastname,email,password):
    data = request.get_json()
    user = User(firstname=data['firstname'],lastname=data['lastname'],email=data['email'],password=data['password'])
    user.token=generate_key()
    user.password = hash_pass(user.password)
    db.session.add(user)
    db.session.commit()
    return "<h1> Success </h1>"

@app.route('/')
def index():
    return jsonify({"hello":"there"})




# @app.route('/', methods=['GET'])
# def send_status():
#     return jsonify({"Status":"Running"})


if __name__ == "__main__":
    app.run(debug=True)