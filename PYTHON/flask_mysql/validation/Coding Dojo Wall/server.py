from flask_app import app
from flask_app.controllers import register
from flask_app.controllers import posts

if __name__ == "__main__":
    app.run(debug=True)
