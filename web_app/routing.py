from flask import render_template
from web_app import app

from web_app.home import home as home_blueprint
app.register_blueprint(home_blueprint)

# register blueprint with prefix
# from db_manager.api import api as api_blueprint
# app.register_blueprint(api_blueprint, url_prefix='/api')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page/errors/404.html', title='Page Not Found'), 404