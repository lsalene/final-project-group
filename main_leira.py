"""
Leira Salene - 1785752

Sufiaan Shaikh - 1869029

CIS-3368-17509

Final Project - Sprint 1 - main.py file
"""

#SUFIAAN (import and setting up application name)
#import flask library from Python
import flask
#Import jsonify to make crud operation in JSON format
from flask import jsonify
from flask import request, make_response
#Import mysql from python to connect vscode to mysql server
from mysql.connector import connect
#Import three sql pre-made functions from sql.py file to establish connection, and execute queries.
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
#setting up the application name
app = flask.Flask(__name__)  # sets up the application
app.config["DEBUG"] = True  # allow to show errors in browser

#creating connection to database from aws
connection = create_connection("cis3368.ctmiynsphvgy.us-east-2.rds.amazonaws.com", "admin", "AWS!cis3368", "cis3368fall21")

#user_table = "CREATE TABLE user( id int(8) AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(55) NOT NULL, last_name VARCHAR(55) NOT NULL)"
#execute_query(connection, user_table)
#restaurant_table = "CREATE TABLE resaturant( restaurant_id int(8) aAUTO_INCREMENT PRIMARY KEY, resaturant_name VARCHAR(55) NOT NULL, user_id INT(8) NOT NULL, FORRIGN KEY (user_id) REFERENCES user(id))"
#execute_query(connection, restaurant_table)

#LEIRA
#default url without any routing as GET request
@app.route('/', methods=['GET'])
def home():
    return "<h1> Deciding Diner!!! </h1>"

#LEIRA
#see all users 
@app.route('/api/user/all', methods=['GET'])
def alluser():
    request_data = request.get_json()
    usersql = "SELECT * FROM user"
    allusers = execute_read_query(connection, usersql) 
    return jsonify(allusers)

#LEIRA
#see all restaurants added
@app.route('/api/restaurant/all', methods=['GET'])
def allrestaurant():
    request_data = request.get_json()
    restaurantsql = "SELECT * FROM restaurant ORDER BY userid"
    allrestaurants = execute_read_query(connection, restaurantsql)
    return jsonify(allrestaurants)

#SUFIAAN
#in case no user is inserted
@app.route('/api/userrestaurant', methods=['GET'])
def userrestaurant_no_userid():
    return 'Please Enter User ID'


@app.route('/api/userrestaurant/<userid>', methods=['GET'])
def userrestaurant(userid):
    request_data = request.get_json()
    usersql = "SELECT * FROM restaurant WHERE userid= '%s'" % (userid)
    alluserrestaurants = execute_read_query(connection, usersql)
    count = len(alluserrestaurants)

    if count > 10:
        return "User has " + str(count) + " restaurants. Max limit is 10."
    elif count < 5:
        return "User has " + str(count) + " restaurants. Add at least 5."
    else:
        return jsonify(alluserrestaurants)
#Please try these examples below, I have users with less than 5, between 5 and 10, and more than 10 restaurants.
#http://127.0.0.1:5000/api/userrestaurant/1  -- 5 restaurants - No error
#http://127.0.0.1:5000/api/userrestaurant/3 -- 11 restaurants - will give error message
#http://127.0.0.1:5000/api/userrestaurant/4 -- 3 restaurants - will give error message


#SUFIAAN
#add new user to sql database
@app.route('/api/adduser', methods=['POST'])
def user():
    request_data = request.get_json()
    new_Fname = request_data['firstname']
    new_Lname = request_data['lastname']
    user_query = "INSERT INTO user(firstname, lastname) values ('%s', '%s')" % (new_Fname, new_Lname)
    execute_query(connection, user_query)
    return "Given Profile Successfully Created!!!"

#SUFIAAN
#add new restaurant according to userid
@app.route('/api/addrestaurant', methods=['POST'])
def restaurant():
    request_data = request.get_json()
    new_rest = request_data['restaurantname']
    user_ID = request_data['userid']
    restaurant_query = "INSERT INTO restaurant(restaurantname, userid) values ('%s', '%s')" % (new_rest, user_ID)
    execute_query(connection, restaurant_query)
    
    return "Given Restaurant Successfully Created!!!"


#LEIRA
#deletes selected user by their id
@app.route('/api/deleteuser', methods=['DELETE'])
def deluser():
    request_data = request.get_json()
    user_ID = request_data['userid']
    user_query = "DELETE FROM user WHERE userid = '%s'" % (user_ID)
    execute_query(connection, user_query)
    return "Selected Profile Successfully Deleted!!!"

#LEIRA
#deletes selected restaurant by id
@app.route('/api/deleterestaurant', methods=['DELETE'])
def delrestaurant():
    request_data = request.get_json()
    restaurantid = request_data['restaurantid']
    user_query = "DELETE FROM restaurant WHERE restaurantid = '%s'" % (restaurantid)
    execute_query(connection, user_query)
    return "Selected Restaurant Successfully Deleted!!!"

#LEIRA
#user is able to update firstname and lastname
@app.route('/api/userupdate', methods=['PATCH'])
def userupdate():
    request_data = request.get_json()
    updated_fname = request_data['firstname']
    updated_lname = request_data['lastname']
    user_ID = request_data['userid']
    userupdate = "UPDATE user SET firstname = '%s', lastname = '%s' WHERE userid = '%s'" % (updated_fname, updated_lname, user_ID)
    execute_query(connection, userupdate)
    return "Selected User Successfully Updated!!!"

#LEIRA
#user is able to update restaurant
@app.route('/api/restaurantupdate', methods=['PATCH'])
def restaurantupdate():
    request_data = request.get_json()
    updated_restaurantname = request_data['restaurantname']
    restaurant_ID = request_data["restaurantid"]
    restaurantupdate = "UPDATE restaurant SET restaurantname = '%s' WHERE restaurantid = '%s'" % (updated_restaurantname, restaurant_ID)
    execute_query(connection, restaurantupdate)
    return "Selected Restaurant Successfully Updated!!!"

#SUFIAAN
#randomize selection for restaurant
@app.route('/api/random', methods=['GET'])
def randomrestaurant():
    request_data = request.get_json()
    randomizedsql = "SELECT restaurantname FROM restaurant ORDER BY RAND() LIMIT 1"
    random_query = execute_read_query(connection, randomizedsql)
    return jsonify(random_query)

app.run()
