from flask import Flask

nextbook = Flask(__name__)

@nextbook.route("/")
def search():
    return "Search: "

@nextbook.route("/results/<filter>/<phrase>")
def results(filter, phrase):
    return f"Search by {filter}: {phrase}"

@nextbook.route("/class-list")
def class_list():
    return "full list"

@nextbook.route("/add-book")
def add_book():
    return "add a book"

@nextbook.route("/about")
def about():
    return "We are cool bros!"

if __name__ == "__main__":
    nextbook.run()
