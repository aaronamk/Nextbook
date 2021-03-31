from flask import Flask, redirect, url_for, request


nextbook = Flask(__name__)


@nextbook.route("/", methods = ['POST', 'GET'])
def search():
    if request.method == "POST":
        test = request.form["phrase"]
        return redirect(url_for('results', filter = "class", phrase = test))
    else:
        test = request.args.get("phrase")
        return redirect(url_for('results', filter = "class", phrase = test))


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
