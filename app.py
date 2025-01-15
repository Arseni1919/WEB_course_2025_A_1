# chrome://net-internals/#sockets
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request, session
import json

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
        logged_user = session['username'] if 'username' in session else 'Stranger'
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


# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# FETCH
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #

@app.route('/fetch_page')
def fetch_page_func():
    return render_template('fetch_example.html')


@app.route('/fetch_example', methods=['GET', 'POST'])
def fetch_example_func():
    if request.method == 'GET':
        data = {'message': 'Success from fetch_example route!'}
        # data = 'Success from fetch_example route!'
        return json.dumps(data)
    elif request.method == 'POST':
        data_dict = request.json
        # check DB
        user_cart = {'orders': 13, 'startDate': '12.1.2024'}
        return json.dumps(user_cart)
    else:
        raise RuntimeError('')

# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# MONGODB
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://1919ars:1919ars@cluster0.kg52uoz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new cluster and connect to the server
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster['mydatabase']
customers_col = mydatabase['customers']
product_col = mydatabase['products']

# sample_analytics_db = cluster['sample_analytics']


@app.route('/mongodb')
def mongodb_func():
    # message = 'good'
    # message = pymongo.version
    # message = cluster.list_database_names()
    # sample_mflix = cluster['sample_mflix']
    # message = sample_mflix.list_collection_names()

    # insert_one
    # take the data from form / from FE
    # my_dict = {
    #     'name': 'Ortal',
    #     'address': 'Aba Hillel 100',
    #     'rating': 19
    # }
    # customers_col.insert_one(my_dict)
    # # # message = cluster.list_database_names()
    # message = my_dict

    # insert_many
    # my_list = [
    #     {'name': 'Tal', 'address': 'Hogwards 37', 'rating': 11},
    #     {'name': 'Bekka', 'address': 'Bronx 3', 'rating': 20},
    #     {'name': 'Alisa', 'address': 'Area 9', 'rating': 30},
    # ]
    # customers_col.insert_many(my_list)
    # message = my_list

    # findOne
    # message = customers_col.find_one({'name': 'John'})

    # find
    # message = list(customers_col.find())

    # find query
    # myquery = {'name': 'John'}
    # message = list(customers_col.find(myquery))
    # myquery = {'rating': {"$gt": 10}}
    # message = list(customers_col.find(myquery))

    # sort
    # myquery = {'rating': {"$gt": 10}}
    # message = list(customers_col.find().sort('name'))
    # message = list(customers_col.find(myquery).sort('name', -1))
    # message = len(list(customers_col.find()))

    # limit
    # message = len(list(customers_col.find()))
    # myquery = {'rating': {"$lt": 50}}
    # message = list(customers_col.find(myquery).sort('rating', -1).limit(3))
    # message = list(customers_col.find().sort('rating', -1).limit(3))

    # update one
    # my_query = {'address': 'Highway 37'}
    # new_values = {'$set': {'address': 'Canyon 123'}}
    # customers_col.update_one(my_query, new_values)
    # message = list(customers_col.find({'address': 'Canyon 123'}))

    # update many
    # customers_col.update_many({}, {'$inc': {'rating': 1}})
    # customers_col.update_many({}, {'$set': {'rating': 100}})
    # message = list(customers_col.find())

    # delete one
    # customers_col.delete_one({'name': 'Ars Perchik'})
    # message = list(customers_col.find())

    # delete many
    # customers_col.delete_many({'rating': {'$gt': 1000}})
    # customers_col.delete_many({'name': 'Tal'})
    # message = list(customers_col.find())

    # aggregations
    # aggregation = [
    #     {
    #         '$match': {
    #             'rating': 100
    #         }
    #     }, {
    #         '$sort': {
    #             'name': -1
    #         }
    #     }, {
    #         '$limit': 5
    #     }
    # ]
    # message = list(customers_col.aggregate(aggregation))
    # message = customers_col.find()
    message = ''
    # return render_template('mongodb_lecture.html', message=message)

    my_list = customers_col.find()
    return render_template('mongodb_lecture.html', my_list=my_list)








@app.route('/db_insert')
def insert_func():
    # insert_one
    my_dict = {
        'name': request.args['name'],
        'address': request.args['address'],
        'rating': int(request.args['rating']),
    }
    customers_col.insert_one(my_dict)
    return redirect(url_for('mongodb_func'))









@app.route('/db_delete', methods=['POST'])
def delete_func():
    print(request.form)
    customers_col.delete_one({'name': request.form['name']})
    return redirect(url_for('mongodb_func'))










@app.route('/db_increment')
def increment_func():
    customers_col.update_many({}, {'$inc': {'rating': 1}})
    return redirect(url_for('mongodb_func'))







