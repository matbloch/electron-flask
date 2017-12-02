import os.path
import sys


# Update PATH to include the local app directory
PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
found_parent_dir = False
for p in sys.path:
    if os.path.abspath(p) == PARENT_DIR:
        found_parent_dir = True
        break
if not found_parent_dir:
    sys.path.insert(0, PARENT_DIR)


if __name__ == '__main__':
    import web_app
    app = web_app.setup_app()
    app.run(host='0.0.0.0', port=4040)
