# Functional imports
from flask import Flask
from config import Config

# Blueprint imports

def get_app():
    # Initialize
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(signup.app)
    return app

app = get_app()

@app.route('/')
def index():
    return "Hello world!"



if __name__ == '__main__':
    app.run(host ='0.0.0.0', port =5000, debug = True)
