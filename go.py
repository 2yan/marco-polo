# Functional imports
from flask import Flask
import flask as f

# Blueprint imports

def get_app():
    # Initialize
    app = Flask(__name__)
    
    # Register blueprints
    return app

app = get_app()

@app.route('/')
def index():
    return f.render_template("home.html")


def get_questions():
    questions = {"Question": ['A', 'B'],
                "Question2": ['C', 'D']
            }



if __name__ == '__main__':
    app.run(host ='0.0.0.0', port =5000, debug = True)
