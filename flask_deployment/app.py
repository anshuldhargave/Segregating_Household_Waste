from flask import Flask

IMAGES_FOLDER = '/Users/anshuldhargave/Desktop/Segregating_Household_Waste/flask_deployment/sample_images'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['IMAGES_FOLDER'] = IMAGES_FOLDER