from flask import Flask, redirect, url_for, request


nextbook = Flask(__name__)


@nextbook.route("/", methods = ['POST', 'GET'])
def search():
    if request.method == "POST":
        phrase = request.form["phrase"]
        filter = request.form["filter"]
        return redirect(url_for('results', filter = filter, phrase = phrase))
    else:
        test = request.args.get("phrase")
        test = request.args.get("filter")
        filter = request.form["filter"]
        return redirect(url_for('results', filter = filter, phrase = phrase))


@nextbook.route("/search?filter=<filter>&q=<phrase>")
def results(filter, phrase):
    if filter not in ["title", "isbn", "class", "professor"]:
        return f"Invalid search filter: {filter}"
    return f"Searched by {filter} for {phrase}"


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
