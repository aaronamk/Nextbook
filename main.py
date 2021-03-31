from flask import Flask

nextbook = Flask(__name__)

@nextbook.route("/")
def home():
    return "Home Page"

@nextbook.route("/full-list")
def full_list():
    return "full list"

if __name__ == "__main__":
    nextbook.run()
