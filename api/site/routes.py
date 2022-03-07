from api.site import blueprint
from flask import render_template 

@blueprint.route('/')
def index():
    return render_template('index.html')