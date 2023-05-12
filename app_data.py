import os
from flask import Flask, render_template, request
import sqlite3 


app = Flask(__name__)  



conn = sqlite3.connect('anxiety.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE IF NOT EXISTS table_anx (name VARCHAR(30), age VARCHAR(30))')
print ("Table created successfully")
conn.close()



@app.route('/')
def home():
    # os.system("python test_anxiety.py")
    return render_template('home.html')

@app.route('/webcam_anx')
def webcam_anx():
    os.system("python test_anxiety.py")
    return render_template('home.html')


@app.route('/qustionary')
def qustionary():
    return render_template('qustionary.html')

@app.route('/add_q1', methods = ['POST', 'GET'])
def add_q1():
    print("hello")
    if request.method == 'POST':
        name = request.form['q1']
        age = request.form['q2']
        print(name,age)

        with  sqlite3.connect("anxiety.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO table_anx(name, age) VALUES(?,?)",(name,age,))

            con.commit()
            msg = "Record Added Successfully"

    else:
       print("enter name and age")

    return render_template('q2.html')
        

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


@app.route('/que7')
def que7():
    return render_template('q7.html')

@app.route('/que8')
def que8():
    return render_template('q8.html')

@app.route('/que9')
def que9():
    return render_template('q9.html')

@app.route('/que10')
def que10():
    return render_template('q10.html')

@app.route('/que11')
def que11():
    return render_template('q11.html')

@app.route('/que12')
def que12():
    return render_template('q12.html')

@app.route('/que13')
def que13():
    return render_template('q13.html')


@app.route('/que14')
def que14():
    return render_template('q14.html')

@app.route('/que15')
def que15():
    return render_template('q15.html')


@app.route('/que16')
def que16():
    return render_template('q16.html')

if __name__ == '__main__':
   app.run(debug=True, port=5000)