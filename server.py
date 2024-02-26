from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'lets guess the number'

@app.route('/')
def home():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1, 100)
    print(session['random_num'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['number_guess']) > int(session['random_num']):
        session['message'] = 'Too high!'
        return redirect('/')
    elif int(request.form['number_guess']) < int(session['random_num']):
        session['message'] = 'Too low!'
        return redirect('/')

if __name__=='__main__':
    app.run(debug=True)