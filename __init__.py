import pymongo
from flask import Flask, render_template, request

app = Flask(__name__)
MONGO_CLIENT = pymongo.MongoClient('mongodb+srv://raswanth:mrraswanth22@greenclub.yu2jugm.mongodb.net/?retryWrites=true&w=majority')
USER_COL = MONGO_CLIENT['greenclub']['users']

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    document = USER_COL.find_one({'username': request.data['username'], 'password': request.data['password']})
    if document:
        return 'localhost/profile.html'
    else:
        return 'localhost/login.html'

@app.route('/register.html')
def register():
    if request.method == 'GET':
        return render_template('register.html')
    USER_COL.insert_one({'username': request.data['username'], 'password': request.data['password'],'email': request.data['email'], 'number': request.data['number']})
    return 'localhost/login.html'

@app.route('/profile.html')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
