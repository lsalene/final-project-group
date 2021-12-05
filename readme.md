# final-project-group
GROUP MEMBERS: Sufiaan Shaikh &amp; Leira Salene

to run the project use command 
1. run main.py file from Sprint1 folder
2. in Sprint2 folder, run --> npm install
3. in Sprint2 folder, run --> node server js  (make sure to use correct path)

CRUD Functionality:

1. All Create, Update, and Delete is working for both restaurant and user pages.
2. userid and restuarant_name has foreign key constrain. So, if you want to delete the user, you need to delete associated restairant first.
--Try deleting Sufiaan Shaikh --> will have alert box.
--Try deleting Ryan Panjwoski --> won't have error because there is no restuarant associated with this user.
3. It will give you an alert box if you want to delete user and it has associated restaurant.
4. If user does not have any restauarnt, it should be deleted without any error.

Maximum Restaurant:
1. If user has already 10 restaurants associated to their id, the add restaurant funtion will not work and instead it will give you the message.
2. Try add more restaurant in Sufiaan Shaikh

References:

for sql.py and main.py file --> referenced from professor's lectures listed below:
1. SQL Operations - Class 4
2. REST API with flask - Class 5

for server.js file and every ejs pages are refereced from professor's lectures listed below:
1. EJS Code - Class 7
2. EJS with APIs and Forms - Class 8


For the Bootstrap:
https://www.tutorialrepublic.com/snippets/preview.php?topic=bootstrap&file=crud-data-table-for-database-with-modal-form


API help for server js file:
https://www.tutorialspoint.com/nodejs/nodejs_restful_api.htm

Alert message box for deleting user:
https://www.w3schools.com/jsref/met_win_alert.asp
https://www.npmjs.com/package/alert

Learning about form groups:
https://www.w3schools.com/bootstrap/bootstrap_forms.asp

Modal-Body for alert message:
https://getbootstrap.com/docs/4.0/components/modal/

Text Boxes for Form Group:
https://www.w3schools.com/bootstrap/bootstrap_forms.asp
