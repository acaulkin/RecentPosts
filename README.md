# Project Description 
This is an API that returns the 100 most recent posts from TechCrunch and stores them within a SQLLite database.

# Time Taken
It took me about 2 hours and 40 minutes to complete the coding, and an extra 20 minutes to write this documentation.

# How I Did It
I did it in a unique way that I feel encapsulates some of the stuff I know how to do with Python in a time-crunch situation.
I decided to store the articles within a SQLLite database, specifically within a table named `Posts`. 
The database is accessed with an included API that contains methods for GET, PUT, and DELETE. 
What do these methods **do?**

GET: Sending a GET request to the API yields all 100 entries within the datbase, which are taken straight from Tech Crunch's website.
You can also send a GET request to a specific post by id. Details on how to do this will be located within the "How To" section.

PUT: Sending a PUT request to the API will update the entries in the databse to be more in line with what's on the site (if some time has passed and new posts go up, it will show those new ones!) It does so by first removing all the entries in the database (I know, probably innefficient) and then re-adds the 100 most recent ones.

DELETE: Sending a DELETE request to the API will...remove all the stuff from the API!

# How To 
## Running The Application
To run the application, first run the following command within your terminal of choice within the project's main directory: </br>
`pip3 install -r requirements.txt` </br>
This installs all of the relevant project dependencies for you. </br>

Next, to run the application, simply use the following command within the project's main directory:
`python3 ./api.py`
This will run the API at the url `http://127.0.0.1:5000/`

## Sending Simple Requests
### Perform All Of These In The Terminal Of Your Choice
GET Request (All Postings): `curl "http://127.0.0.1:5000/posts"` </br>
GET Request (Individual Posting): `curl "http://127.0.0.1:5000/posts/<post-id-goes-here>"` </br>
PUT Request: `curl "http://127.0.0.1:5000/posts -X PUT`  </br>
DELETE Request: `curl "http://127.0.0.1:5000/posts -X DELETE` 

## Performing Simple Included Unit Test
The simple unit test makes sure there are 100 values within the SQL database.
To perform the test, run the following command within the application's main directory: </br>
`python3 ./test.py`

# Data Model
| Key Value  | Content |
| ------------- | ------------- |
| id  | id of the article  |
| title  | title of the article  |
| author  | author of the article  |
| date  | date the article was created  |
| url  | url to the article  |
| content  | all the rendered text for the article's content  |
