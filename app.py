from flask import Flask, render_template, request

app = Flask(__name__)

if __name__ == "__name__":
    app.run()

@app.route('/')
def index():
    return render_template('index.html')

    