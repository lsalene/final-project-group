//Leira Salene - 

//Sufiaan Shaikh - 1869029

//CIS-3368-17509

//Final Project - Sprint 2 - server file



// load the express 
var express = require('express');
var app = express();
const bodyParser = require('body-parser');
const apiEndPoint = "http://127.0.0.1:5000/api/"; // assign a const to call api from port 5000 --> just need to change path for differnt pages


// required module to make calls to a REST API
const axios = require('axios');

//to display alert messages
let alert = require('alert');


app.use(bodyParser.urlencoded());
// set the view engine to ejs
app.set('view engine', 'ejs');




// when application firstrun redirect to home page
app.get("/", function (req, res) {
    LoadHomePage(res);
});

//Sufiian Shaikh
//for manage-user page
//this will call the api '/api/user/all' from main.py file and list all users there --> it is also a homepage for out GUI
app.get('/user', function (req, res) {    //get method to show all users on homepage
    LoadHomePage(res);
});

function LoadHomePage(res) {
    let results = [];
    // connecting python API --> apiEndPoint const we defined above
    axios.get(apiEndPoint + 'user/all') //calling all the available users from user/api and render them to mange-user.ejs page
        .then((response) => {
            if (response && response.data) {
                results = response.data;
                res.render("pages/user/manage-user.ejs", { data: results });//render the results in manage-user.ejs page to show all data and add new user button
            }
            else {
                res.render("pages/user/manage-user.ejs", { data: results });
            }
        });
}

//Sufiaan Shaikh
//Adding a new user to the user table from GUI
app.get('/add-user', function (req, res) {    //get method to show the elements of the add-user.ejs page in browser
    res.render("pages/user/add-user.ejs", { data: null }); //render new user to add-user.ejs page
});
// redirecting to the api/user from python file, and adding user in the database
app.post('/add-user', function (req, res) {    //post method to add new users in GUI and Database
    axios.post(apiEndPoint + 'user', req.body)   //calling user api in POST method to add new users in the Databse
        .then((response) => {
            res.redirect('/user');   //After adding new users it will redirect to the /user page in browsser
        });
});

//Sufiaan Shaikh
//display all available restaurants in /restaurant page using get method
app.get('/restaurant', function (req, res) {
    let results = [];   //hold results into a variable
    axios.get(apiEndPoint + 'restaurant/all')      //calling /restaurant/all api from python file to show all restaurant using get method
        .then((response) => {
            if (response && response.data) {
                results = response.data;     //adding all available restaurants in results
                res.render("pages/restaurant/manage-restaurant.ejs", { data: results, message: null });   //render the data manage-restaurant.ejs page to show data and add new restaurant button
            }
            else {
                res.render("pages/restaurant/manage-restaurant.ejs", { data: results, message: null });
            }
        });
});



// Server setup
app.listen(8080, () => {
    console.log(
        `8080 is a Magic Port`);
});



