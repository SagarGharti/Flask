import os
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir,'content.db'))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = database_file
db = SQLAlchemy(app)
@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/category')
def category():
    return render_template('category.html')
@app.route('/register')
def register():
    return render_template('register.html')    
@app.route('/post')
def post():
    return render_template('post.html')    
if __name__ == '__main__':
    app.run()
    