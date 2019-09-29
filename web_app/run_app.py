import os.path
import sys


if __name__ == '__main__':
    import web_app
    app = web_app.setup_app()
    app.run(host='0.0.0.0', port=4040, debug=False)
