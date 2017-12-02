from flask import Flask


# setup Flask app
app = Flask(__name__, static_url_path='/static')

# debug: reload jinja templates
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

# remove cache limit (default is 50 templates)
app.jinja_env.cache = {}


def setup_app():

    # setup routing
    from web_app import routing

    return app



