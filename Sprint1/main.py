"""
Leira Salene - 

Sufiaan Shaikh - 1869029

CIS-3368-17509

Final Project - Sprint 1 - main.py file
"""

#import flask library from Python 
import flask
#Import jsonify to make crud operation in JSON format
from flask import jsonify
from flask import request, make_response
#Import mysql from python to connect vscode to mysql server
from mysql.connector import connect
from mysql.connector.connection import MySQLConnection
#Import three sql pre-made functions from sql.py file to establish connection, and execute queries.
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

import random

#setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show errors in browser

#creating connection to Database stored in AWS using AWS credentials.
connection = create_connection("cis3368.cmvgv3q08uqc.us-east-1.rds.amazonaws.com", "admin", "S^Richmond9", "cis3368fall21")


#user_table = "CREATE TABLE user( id int(8) AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(55) NOT NULL, last_name VARCHAR(55) NOT NULL)"
#execute_query(connection, user_table)

#restaurant_table = "CREATE TABLE restaurant(restaurant_ int(8) AUTO_INCREMENT PRIMARY KEY, restaurant_name VARCHAR(55) NOT NULL, user_id INT(8) NOT NULL, FORRIGN KEY (user_id) REFERENCES user(id))"
#execute_query(connection, restaurant_table)

#API 1 This is GET method API. It will return the welcome text to the web browser - Sufiaan Shaikh
@app.route('/', methods=['GET']) # default url without any routing as GET request
def home():
    return "<h1> Deciding Diner!!! </h1>"

#API 2 This API will return all users availabe in user table in json format - Leira Salene
@app.route('/api/user/all', methods=['GET'])
def alluser():
    request_data = request.get_json()
    usersql = "SELECT * FROM user"
    allusers = execute_read_query(connection, usersql) 
    return jsonify(allusers)

#API 3 This API will return all restaurants name and associated user id in json format - Leira Salene
@app.route('/api/restaurant/all', methods=['GET'])
def allrestaurant():
    request_data = request.get_json()
    restaurantsql = "SELECT r.*,a.first_name,a.last_name FROM restaurant as r,user as a where r.user_id=a.id  ORDER BY user_id"
    allrestaurants = execute_read_query(connection, restaurantsql)
    return jsonify(allrestaurants)

#API 4 This API only returns a message if no user is inserted - Sufiaan Shaikh
@app.route('/api/userrestaurant', methods=['GET'])
def userrestaurant_no_user_id():
    return 'Enter User ID'

#API 5 This API will return between 5 and 10 restaurants according to user id. If user has inserted less than 5 and more than 10 restaurants, it will show error message. - Sufiaan Shaikh 
@app.route('/api/userrestaurant/<user_id>', methods=['GET'])
def userrestaurant(user_id):
    request_data = request.get_json()
    usersql = "SELECT * FROM restaurant WHERE user_id=" + user_id
    alluserrestaurants = execute_read_query(connection, usersql) 
    count = len(alluserrestaurants)
    
    if count > 10:
        return "User have " + str(count) + " restaurants. Max limit is 10."
    elif count < 5:
        return "User have " + str(count) + " restaurants. Add at least 5."
    else:
        return jsonify(alluserrestaurants)
#Please try these examples below, I have users with less than 5, between 5 and 10, and more than 10 restaurants.
#http://127.0.0.1:5000/api/userrestaurant/1  -- 5 restaurants - No error
#http://127.0.0.1:5000/api/userrestaurant/3 -- 11 restaurants - will give error message
#http://127.0.0.1:5000/api/userrestaurant/4 -- 3 restaurants - will give error message

#API 6 POST method to add users into user table - Sufiaan Shaikh
@app.route('/api/user', methods=['POST'])
def user():
    request_data = request.get_json()
    new_Fname = request_data['first_name']
    new_Lname = request_data['last_name']

    user_query = "INSERT INTO user(first_name, last_name) values ('%s', '%s')" % (new_Fname, new_Lname)

    execute_query(connection, user_query)
    return 'Given Profile Successfully Created!!!'

#API 7 POST method to add restaurants in restaurant table - Sufiaan Shaikh
@app.route('/api/restaurant', methods=['POST'])
def restaurant():
    request_data = request.get_json()
    new_Rname = request_data['restaurant_name']
    new_Id = request_data['user_id']

    # check user resturant count
    usersql = "SELECT * FROM restaurant WHERE user_id=" + new_Id
    alluserrestaurants = execute_read_query(connection, usersql) 
    count = len(alluserrestaurants)

    if count>=10 :
        return "False"
    else :
        restaurant_query = "INSERT INTO restaurant(restaurant_name, user_id) values ('%s', '%s')" % (new_Rname, new_Id)
        execute_query(connection, restaurant_query)
        return "True"
    

    

#API 8 DELETE Method to delete user from user table - Leira Salene
@app.route('/api/deleteuser/<id>', methods=['DELETE'])
def deluser(id):
    # check user resturant count
    usersql = "SELECT * FROM restaurant WHERE user_id=" + id
    alluserrestaurants = execute_read_query(connection, usersql) 
    count = len(alluserrestaurants)
    if count==0:
        del_user_query = "DELETE FROM user WHERE id = '%s'" % (id)
        execute_query(connection, del_user_query)
        return "Selected Profile Successfully Deleted!!!"
    else :
        return "False"



#API 9 DELETE Method to delete restaurant from restaurant table - Leira Salene
@app.route('/api/deleterestaurant/<restaurant_id>', methods=['DELETE'])
def delrestaurant(restaurant_id):
    # request_data = request.get_json()
    # restaurantid = request_data['restaurant_id']

    del_rest_query = "DELETE FROM restaurant WHERE restaurant_id = '%s'" % (restaurant_id)
    execute_query(connection, del_rest_query)
    return "Selected Restaurant Successfully Deleted!!!"

#API 10 PATCH Method to update user in user table - Leira Salene
@app.route('/api/userupdate', methods=['PATCH'])
def userupdate():
    request_data = request.get_json()
    updated_fname = request_data['first_name']
    updated_lname = request_data['last_name']
    user_ID = request_data['id']
    userupdate = "UPDATE user SET first_name = '%s', last_name = '%s' WHERE id = '%s'" % (updated_fname, updated_lname, user_ID)
    execute_query(connection, userupdate)
    return "Selected User Successfully Updated!!!"

#API 11 Patch Method to update restaurants in restaurant table - Leira Salene
@app.route('/api/restaurantupdate', methods=['PATCH'])
def restaurantupdate():
    request_data = request.get_json()
    updated_restaurantname = request_data['restaurant_name']
    restaurant_ID = request_data["restaurant_id"]
    restaurantupdate = "UPDATE restaurant SET restaurant_name = '%s' WHERE restaurant_id = '%s'" % (updated_restaurantname, restaurant_ID)
    execute_query(connection, restaurantupdate)
    return "Selected Restaurant Successfully Updated!!!"

#API 12 GET method to return random selected restaurant in json method. - Sufiaan Shaikh
@app.route('/api/random', methods=['GET'])
def randomrestaurant():
    request_data = request.get_json()
    randomInt=random.randint(2, 5)   #using random library, generating random numbers between 2 and 5
    #this query will group the random people and assign them one random restaurant
    random_sql = """ select Restaurant.restaurant_name,GROUP_CONCAT(user.first_name) as  first_name
                     from 
                     (SELECT  restaurant_name
                     from 
                     restaurant
                     ORDER BY RAND() limit 1) as Restaurant,
                     (select first_name from user ORDER BY RAND() limit %s) as user """ %(randomInt)
    random_query = execute_read_query(connection, random_sql)
    return jsonify(random_query)

#Api 13 Get method to get user detail by id - Sufiaan Shaikh
@app.route('/api/user/<id>', methods=['GET'])
def getUserByID(id):
    #getting user based on id provided. It is helpful in frontend to edit the user
    restaurantsql = "SELECT * FROM user WHERE id = '%s'" % (id)
    user = execute_read_query(connection, restaurantsql)
    return jsonify(user)


#Api 14 Get method to get resturant detail by resturant id - Leira Salene
@app.route('/api/restaurant/<restaurant_id>', methods=['GET'])
def getRestaurantByID(restaurant_id):
    #getting restaurant based on id provided. It is helpful in frontend to edit  the restaurant
    restaurantsql = "SELECT * FROM restaurant WHERE restaurant_id = '%s'" % (restaurant_id)
    restaurant = execute_read_query(connection, restaurantsql)
    return jsonify(restaurant)



app.run()
