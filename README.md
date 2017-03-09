# Faver v0.1.0
####Your Favorite Flickr Photos in One Place

## Installation

`git clone https://github.com/jeffkwiat/virta-flickr.git`

`source bin/activate`

`pip install -r requirements.txt`

## Known Issues

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
