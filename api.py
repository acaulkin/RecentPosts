from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import requests
import json 

# Configuring the application and database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.sqlite"
api = Api(app)
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, unique = True, nullable = False)
    author = db.Column(db.Integer, unique = False, nullable = False)
    date = db.Column(db.String, unique = False, nullable = False)
    url = db.Column(db.String, unique = True, nullable = False)
    content = db.Column(db.String, unique = False, nullable = False)

class TechCrunchPostings(Resource):
    def get(self):
        """
        This method will return all 100 values from the database that contains
        all the 100 most recent values from TechCrunch's 100 most recent postings
        """
        
        # Getting all the values within the database
        posts = Post.query.all()

        # Storing all posts in a list of dictionaries for easy export
        markersToSend = []
        for post in posts:
            tempDictionary = {
                'id': post.id,
                'title': post.title,
                'author': post.author,
                'date': post.date,
                'url': post.url,
                'content': post.content
            }
            markersToSend.append(tempDictionary)

        return markersToSend

    def put(self):
        """
        This method when called, will update the values within the database to 
        be in-line with what is actually on TechCrunch's page
        """

        # Removing the current values within the database
        Post.query.delete()
        db.session.commit()

        # Trying to hit the WP API
        try:
            techCrunchResponse = requests.get('https://techcrunch.com/wp-json/wp/v2/posts?per_page=100')
            responseContent = json.loads(techCrunchResponse.content)
        except requests.exceptions.RequestException as e:
            raise e

        # If successful, parse the response content and create a new Post object
        for jsonObject in responseContent:
            try:
                jsonObject = dict(jsonObject)
                newPost = Post(
                    id = jsonObject['id'],
                    title = jsonObject['title']['rendered'],
                    author = jsonObject['author'],
                    date = jsonObject['date'],
                    url = jsonObject['shortlink'],
                    content = jsonObject['content']['rendered']
                )
            except:
                print('ERROR: Missing key value within dictionary.')

            # Insert the new post into the database
            db.session.add(newPost)
            # Committing changes
            db.session.commit()
            # Making sure to close out connection to the database
            db.session.close()            

        return 'Successfully updated all of the database values!'

    def delete(self):
        """
        This method when called will remove all entries from the database
        """

        Post.query.delete()

        # Committing changes
        db.session.commit()
        # Making sure to close out connection to the database
        db.session.close()
        
        return 'All values successfully removed!'


class TechCrunchPostingsById(Resource):
    def get(self, id):
        """
        This method will return the post by Id value; e.g., when the URL is 
        sent a request like so: localhost/posts/id it will return only that
        post's "important stuff"
        """

        # Retrievining individual post
        postToReturn = Post.query.get(id)
        # If post exists, convert to dictionary for easy export back to user
        if postToReturn:
            postToReturn = {
                'id': postToReturn.id,
                'title': postToReturn.title,
                'author': postToReturn.author,
                'date': postToReturn.date,
                'url': postToReturn.url,
                'content': postToReturn.content
            }

            return postToReturn
        else:
            return 'Error: Post With That Id Not Found. Please Try Again.'


api.add_resource(TechCrunchPostings, '/posts')
api.add_resource(TechCrunchPostingsById, '/posts/<id>')

if __name__ == '__main__':
    app.run(debug = True)