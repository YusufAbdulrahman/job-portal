from flask import Flask, render_template, request, redirect
from db import mydb, mycursor


app = Flask(__name__)

@app.route('/')
def index():
    mycursor.execute("SELECT * FROM emp")
    emp = mycursor.fetchall()
    return render_template('index.html', emp = emp)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        fname = request.form['fname']
        mname = request.form['mname']
        lname = request.form['lname']
        address = request.form['address']
        state = request.form['state']
        phone = request.form['phone']
        emeil = request.form['emeil']
        age = request.form['age']
        y_work = request.form['y_work']
        sql = 'INSERT INTO emp (fname, mname, lname, address, state, phone, emeil,  age, y_work) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (fname, mname, lname, address, state, phone, emeil, age, y_work)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/')


@app.route('/workers')
def work():
    mycursor.execute("SELECT * FROM emp")
    emp = mycursor.fetchall()
    return render_template('workers.html', emp = emp)    


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM emp WHERE ID={id}')
        emp = mycursor.fetchone()
        return render_template('edit.html', emp = emp)
    if request.method == 'POST':
        fname = request.form['fname']
        mname = request.form['mname']
        lname = request.form['lname']
        address = request.form['address']
        state = request.form['state']
        phone = request.form['phone']
        emeil = request.form['emeil']
        age = request.form['age']
        y_work = request.form['y_work']
        sql = f'UPDATE emp SET fname = %s, mname = %s, lname = %s, address = %s, state = %s, phone = %s, emeil = %s, age = %s, y_work = %s, WHERE ID = %s'
        values =  (fname, mname, lname, address, state, phone, emeil, age, y_work)
        mycursor.execute(sql, values)
        mydb.commit()
        return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    sql = f'DELETE FROM emp WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run()