from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def greet ():
    return "hi"

if __name__ == "__main__":
    app.run()