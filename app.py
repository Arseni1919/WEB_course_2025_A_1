# chrome://net-internals/#sockets
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request, session

app = Flask(__name__)
app.secret_key = '123'

@app.route('/index')
@app.route('/home')
@app.route('/')
def main_page():
    # from DB import client name and last name
    user = {
        'first_name': 'Ariel',
        'last_name': 'Felner',
        'age': 50,
    }
    # user = None
    hobbies = ['Prog', 'Painting']
    degrees = ('B.Sc.', 'M.Sc.')

    return render_template('index.html',
                           user=user,
                           hobbies=hobbies,
                           degrees=degrees
                           )


# @app.route('/about', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/about', methods=['GET', 'POST'])
def about_page():
    return render_template('about.html')


@app.route('/customers')
def customers_page():
    # return redirect('/')
    return redirect(url_for('main_page'))


@app.route('/products')
def products_page():
    return 'Welcome to PRODUCTS Page!'


@app.route('/customer/5/cart')
def cart_page():
    return 'Inside CART!'


################################
################################
################################

@app.route('/block_example')
def block_example_func():
    return render_template('block_example.html')


@app.route('/request_response', methods=['GET', 'POST'])
def request_response_func():
    request_type = request.method
    if request_type == 'GET':
        logged_user = session['username']
        if 'first_name' in request.args:
            first_name = request.args['first_name']
            last_name = request.args['last_name']
            return render_template(
                'request_example.html',
                request_type=request_type,
                first_name=first_name,
                last_name=last_name,
                logged_user=logged_user
            )
        return render_template(
            'request_example.html',
            request_type=request_type,
            logged_user=logged_user
        )
    elif request_type == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        # checking with DB
        # return redirect(url_for('main_page'))
        return render_template(
            'request_example.html',
            request_type=request_type,
            user_name=user_name,
            password=password
        )


@app.route('/login', methods=['GET', 'POST'])
def log_in_func():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['user_name']
    password = request.form['password']
    # checking with DB
    pass
    # if user is valid -> save the username inside the session
    session['username'] = username
    session['logged_in'] = True
    session['user_data'] = {'second_name': 'Katz', 'tel': 123}
    # return redirect(url_for('main_page'))
    return redirect('/')


@app.route('/logout')
def logout_func():
    session['username'] = None
    session['logged_in'] = False
    # return redirect(url_for('main_page'))
    return redirect('/')


# http://127.0.0.1:5000
# /request_response
# ?
# first_name=Arseniy
# &
# last_name=Pertzovsky