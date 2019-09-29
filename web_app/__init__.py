from flask import Flask
import os, sys

base_dir = '.'
# Check if the application runs in a bundled executable from PyInstaller.
# When executed, the bundled executable get's unpacked into the temporary directory sys._MEIPASS
if hasattr(sys, '_MEIPASS'):
    base_dir = os.path.join(sys._MEIPASS)

app = Flask(__name__,
        static_folder=os.path.join(base_dir, 'static'),
        template_folder=os.path.join(base_dir, 'templates'))

# debug: reload jinja templates
#app.jinja_env.auto_reload = True
#app.config['TEMPLATES_AUTO_RELOAD'] = True

# remove cache limit (default is 50 templates)
app.jinja_env.cache = {}


def setup_app():
    # setup routing
    from web_app import routing
    return app
