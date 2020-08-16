from app import create_app

# NOTE: Explicitly import configuration so that PyInstaller is able to find and bundle it
import config

application = create_app("config.DevelopmentConfig")

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=4040)
