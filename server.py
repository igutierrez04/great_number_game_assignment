from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'lets guess the number'

@app.route('/')
def home():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1, 100)
    if 'count' not in session:
        session['count'] = 0
    print(session['random_num'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['number_guess']) > int(session['random_num']):
        session['message'] = 'too high!'
        session['count'] += 1
        print(session['count'])
        return redirect('/')
    elif int(request.form['number_guess']) < int(session['random_num']):
        session['message'] = 'too low!'
        session['count'] += 1
        print(session['count'])
        return redirect('/')
    else:
        if int(request.form['number_guess']) == int(session['random_num']):
            session['message'] = 'correct!'
            return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)