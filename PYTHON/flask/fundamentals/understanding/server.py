from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<name>')
def say_name(name):
    return f'Hi {name}!'


@app.route('/repeat/<string:name>/<int:number>')
def multiply_name(name, number):
    return f'Hi {name * number}!'


@app.route('/coding/dojo/rules')
def coding_Dojo_Rules():
    return "Hello Awesome Developer"


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

# import statements, maybe some other routes
exit
