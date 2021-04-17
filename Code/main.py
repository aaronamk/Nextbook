from urllib.parse import quote_plus
from flask import Flask, redirect, url_for, render_template, request, g
import sqlite3 as sql

nextbook = Flask(__name__)
database = '/database/database.db'

def get_db():
    if 'db' not in g:
        g.db = sql.connect(database)
        g.db.row_factory = sql.Row
    return g.db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

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

@nextbook.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    nextbook.run(debug = True)
