from urllib.parse import quote_plus
from flask import Flask, redirect, url_for, render_template, request


nextbook = Flask(__name__)


@nextbook.route("/", methods = ['GET', 'POST'])
def search():
    if request.method == "POST":
        phrase = quote_plus(request.form["phrase"])
        if phrase == "":
            return render_template("search.html")
        filter = quote_plus(request.form["filter"])

        return redirect(f"search?filter={filter}&q={phrase}")
    else:
        return render_template("search.html")


@nextbook.route("/search")
def results():
    return render_template("results.html")

@nextbook.route("/class-list")
def course_list():
    return render_template("major-directory.html")


@nextbook.route("/add-book", methods = ['GET', 'POST'])
def add_book():
    if request.method == "POST":
        in_isbn = request.form["isbn"]
        in_title = request.form["title"]
        in_author = request.form["author"]
        in_professor = request.form["professor"]
        in_course = request.form["course"]

        # TODO: interface with the database here to add the book

        return redirect(url_for("book_page", isbn = in_isbn))
    else:
        return render_template("add-book.html")


@nextbook.route("/book/<isbn>")
def book_page(isbn):
    return render_template("book-info.html",
                                isbn = isbn,
                               title = "Introduction to Algorithms",
                              author = "Thomas H. Cormen",
                           professor = "Peter Kemper",
                              course = "CSCI 303, Algorithms")


@nextbook.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    nextbook.run(debug = True)
