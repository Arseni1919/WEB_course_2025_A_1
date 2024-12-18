# chrome://net-internals/#sockets
from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)

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
