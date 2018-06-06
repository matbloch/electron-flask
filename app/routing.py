from flask import render_template
from web_app import app

from web_app.home import home as home_blueprint
app.register_blueprint(home_blueprint)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page/errors/404.html', title='Page Not Found'), 404
	