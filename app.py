from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://chikoid:chiko123@chikobase.oi5ykjl.mongodb.net/')
db = client.buyingland

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    
    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }

    db.lands.insert_one(doc)
    
    return jsonify({'msg': 'successfully to buy!'})

@app.route("/mars", methods=["GET"])
def mars_get():
    lands_list = list(db.lands.find({},{'_id':False}))
    return jsonify({'lands':lands_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)