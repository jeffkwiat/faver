# Faver v0.1.0
####Your Favorite Flickr Photos in One Place

## Installation

#### 2) Setup a virtualenv:
`$ sudo pip install virtualenv`

`$ virtualenv -p python3 virta-flickr`

`$ cd virta-flickr`

`$ source bin/activate`

#### 2) Clone the repository:
`git clone https://github.com/jeffkwiat/virta-flickr.git`

#### 3) Clone the repository:
`pip install -r requirements.txt`

#### 4) Setup your environment variables:
`export FLASK_APP=app.py`

`export FLASK_DEBUG=1`

#### 5) Run the app:
`flask run`

#### 6) Point your browser to:
`http://localhost:5000`

## Time Spent: 7.5 hours

## Difficulties
* I had not coded in ReactJS much previously, so I ran into a few newbie issues (CORS-related, passing data from ReactJS-to-Flask, library installations, etc.).  This project was a great learning experience!
* The JQuery CDN was up and down for a couple hours, so I downloaded a copy of the file locally.
* I am currently having an issue with passing the current Photo's information back to the server, to Fave/UnFave.

### General
* Update README

### Design
* Consider different templates
* Replace logo with something that includes the name.
* Integrate react-gallery or a better grid layout overall.

### Functionality
* Consider replacing $.ajax with axios (et. al.)?
* Integrate Flask-Rest
* Consider moving JQuery back to a CDN

### Testability
* Add more pytests
* Add mocha for javascript tests
* Improve coverage

### Scalability
* Migrate to PostgreSQL
* Migrate to AWS
* Add Redux

### Security
* Integrate Flask-Login
* We're using uuid.uuid4() which generates a random UUID.  Should we use something different?