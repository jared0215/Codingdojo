from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


@app.route('/coding/dojo/rules')
def coding_Dojo_Rules():
    return "Hello Awesome Developer"

# The "@" decorator associates this route with the function immediately following
# @app.route('/')
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

# import statements, maybe some other routes
