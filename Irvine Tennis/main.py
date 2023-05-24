from flask import Flask, render_template, request
import random
app = Flask(__name__)
idnumbers = []

def getidnum():
    id = random.randint(999, 9999)
    if id in idnumbers:
        getidnum()
    else:
        idnumbers.append(id)
        return id

class customer:
    string_name = 'not given'
    string_type = 'not given'
    string_tension = 'not given'
    string_date = 'not given'
    string_number = 'not given'
    string_dp = 'not given'
    string_id = '0'


customer


@app.route('/text', methods = ['POST', 'GET'])
def confirm():

        return render_template('text.html', id=customer.string_id)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/print')
def print():
    return render_template('print.html')


@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        customer.string_fname = request.form['fname']
        customer.string_type = request.form['string']
        customer.string_tension = request.form['tension']
        customer.string_date = request.form['date']
        customer.string_number = request.form['number']
        customer.string_dp = request.form['pay']
        customer.string_id = getidnum()

        idnumbers.append(customer.string_id)

        return render_template('updatecustomer.html', name = customer.string_fname, type = customer.string_type, tension = customer.string_tension, date = customer.string_date, number = customer.string_number, dp = customer.string_dp, id = customer.string_id)
    else:
        return render_template('fail.html')


@app.route('/done')
def done():
    if request.method == 'POST':
        done_id = request.form['complete_id']
        if done_id in idnumbers:
            idnumbers.remove(done_id)
    return render_template('done.html')


if __name__ == "__main__":
    app.run()