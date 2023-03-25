from flask import Flask, render_template
app = Flask(__name__)


@app.route('/<string:name>/<int:num>')
def index(name, num):
    # notice the 2 new named arguments!
    return render_template("index.html", name=name, num=num)


if __name__ == "__main__":
    app.run(debug=True)
