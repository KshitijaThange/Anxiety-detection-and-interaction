import os
from flask import Flask, render_template, request
# import sqlite3
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///questions.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class qustionary(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
    
#     def __repr__(self):
#         return '<Name %r>' % self.id


@app.route('/')
def home():
    # os.system("python test_anxiety.py")
    return render_template('home.html')

@app.route('/webcam_anx')
def webcam_anx():
    os.system("python test_anxiety.py")
    return render_template('home.html')

@app.route('/qustionary', methods = ['POST', 'GET'])
def qustionary():
   
    return render_template('qustionary.html')
        

@app.route('/que2')
def que2():
    return render_template('q2.html')


@app.route('/que3')
def que3():
    return render_template('q3.html')

@app.route('/que4')
def que4():
    return render_template('q4.html')


@app.route('/que5')
def que5():
    return render_template('q5.html')

@app.route('/que6')
def que6():
    return render_template('q6.html')

if __name__ == '__main__':
   app.run(debug=True, port=5000)