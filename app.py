from flask import Flask, json, request, jsonify
from flask_cors import CORS
import time

class User:
    def __init__(self,name,gender, username, password, email):
        self.name = name
        self.gender = gender
        self.username = username
        self.password = password
        self.email = email


app = Flask(__name__)
CORS(app)

users = []
#C
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    name = data["name"]
    gender = data["gender"]
    username = data["username"]
    password = data["password"]
    email = data["email"]
    for user in users:
        if user.email == email:
            return jsonify({"message": "email repeated"}), 400
    users.append(User(name,
                 gender, username, password, email))
    return jsonify(request.get_json()), 200


@app.route("/login", methods = ["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    for user in users:
        if user.email == email:
            if user.password == password:
                return jsonify({
                    "name" : user.name,
                    "gender" : user.gender,
                    "username" : user.username,
                    "email" : user.email
                }), 200
            else:
                return jsonify({
                    "message" : "bad credentials"
                }), 400
    return jsonify({
        "message": "user not found"
    }), 400    
#D
@app.route("/delete", methods = ["DELETE"])
def delete():
    data = request.get_json()
    username = data["username"]
    for user in users:
        if user.username == username:
            #users.remove(user)
            return jsonify({
                "message": "user delete"
            }),200
        else:
            return jsonify({
                    "message" : "user no exist"
                }), 400
#U  
@app.route("/modify", methods = ["PUT"])
def modify():
    data = request.get_json()
    username = data["username"]
    for user in users:
        if user.username == username:
            return jsonify({
                "error": "arg invalid"
            }),400
        else:
            user.username = data["username"] 
            user.name = data["name"]   
            user.password = data["password"]
            user.email = data["email"]
            return jsonify({
                "name" : user.name,
                "gender" : user.gender,
                "username" : user.username,
                "email" : user.email
            }), 200 
#R        
@app.route("/cargar", methods = ["GET"])
def cargar():
    if request.method == "GET":
        tmp = []
        for user in users:
            tmp.append({"username": user.username, "name": user.name, "gender" : user.gender})    
        return jsonify(tmp),200        
app.run(port=5000)        