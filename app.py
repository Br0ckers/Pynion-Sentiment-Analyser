from flask import request, jsonify, Flask, redirect, render_template, session, abort, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        'index.html')

@app.route("/test")
def test():
    return render_template(
        'test.html')

if __name__ == "__main__":
    app.run()
