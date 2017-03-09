# Faver v0.1.0
####Your Favorite Flickr Photos in One Place

## Installation

`git clone https://github.com/jeffkwiat/virta-flickr.git`

`source bin/activate`

`pip install -r requirements.txt`

`export FLASK_APP=app.py`

`export FLASK_DEBUG=1`

`flask run`

## Time Spent: 6.0 hours

## Difficulties
* I had not coded in ReactJS much previously, so I ran into a few newbie issues (CORS-related, passing data from ReactJS-to-Flask, library installations, etc.).  This project was a great learning experience!
* I initially attempted a all-in solution, involving Docker containers on AWS, with React/Redux/Flask/MaterialUI, but I realized it was a bit much for this project, so I scaled it back and focused on the functionality.

### General
* Update README

### Design
* Grab a Template
* Create an actual logo
* Integrate react-gallery or a better grid layout overall

### Functionality
* Review replacing $.ajax with axios (et. al.)?
* Integrate Flask-Rest
* Consider moving JQuery back to a CDN

### Testability
* Add Tests

### Scalability
* Migrate to PostgreSQL
* Migrate to AWS
* Add Redux

### Security
* Integrate Flask-Login
* We're using uuid.uuid4() which generates a random UUID.  Should we use something different?