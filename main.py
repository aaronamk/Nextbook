from flask import Flask

nextbook = Flask(__name__)

@nextbook.route("/")
def home():
    return "Home Page"

@nextbook.route("/class-list")
def class_list():
    return "full list"

@nextbook.route("/add-book")
def full_list():
    return "add a book"

@nextbook.route("/about")
def full_list():
    return "We are cool bros!"

if __name__ == "__main__":
    nextbook.run()
