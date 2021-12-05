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
app.get("/", (req, res) => {
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





// Server setup
app.listen(8080, () => {
    console.log(
        `8080 is a Magic Port`);
});



