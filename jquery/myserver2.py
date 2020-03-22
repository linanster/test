# coding:utf-8
 
from flask import *
from flask import request
 
app = Flask(__name__, template_folder='.')
 
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)
 
@app.route('/')
def index():
    html=render_template('index2.html')
    return html
 
 
if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")
