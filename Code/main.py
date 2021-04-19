from urllib.parse import quote_plus
from flask import Flask, redirect, url_for, render_template, request, g
import sqlite3 as sql

nextbook = Flask(__name__)


def get_db():
    if "db" not in g:
        g.db = sql.connect("database/database.db")
        g.db.row_factory = sql.Row
    return g.db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    g.db.commit()
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@nextbook.route("/", methods = ["GET", "POST"])
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
    if request.args["filter"] == "isbn":
        return redirect(url_for("book_page", isbn = request.args["q"]))

    # print all the textbooks cause it's cool
    for row in query_db("SELECT * FROM textbook"):
        print(row[0],row[1],row[2])

    return render_template("results.html")


@nextbook.route("/class-list")
def course_list():
    return render_template("major-directory.html")


@nextbook.route("/add-book", methods = ["GET", "POST"])
def add_book():
    if request.method == "POST":
        in_isbn = int(request.form["isbn"])
        in_title = request.form["title"]
        in_author = request.form["author"]
        in_professor = request.form["professor"]
        in_course = request.form["course"]

        query_db(f"INSERT INTO textbook (isbn, title, author) VALUES ('{in_isbn}','{in_title}','{in_author}');")

        return redirect(url_for("book_page", isbn = in_isbn))
    else:
        return render_template("add-book.html")


@nextbook.route("/book/<isbn>", methods = ["GET", "POST"])
def book_page(isbn):
    count, total_score = 0, 0
    for score in query_db("select * from review where isbn = ?", [isbn]):
        count += 1
        total_score += score["score"]
    if (count!=0):
        total_score = round(total_score/count,1)
    if request.method== "POST":
        in_price = request.form["price"]
        in_link = request.form["link"]
        #TODO interface with database then directly #return redirect(url_for("book_page", isbn = isbn))
        # for now to show price and url changes\
        return render_template("book-info.html",
                                isbn = isbn,
                               title = "Introduction to Algorithms",
                              author = "Thomas H. Cormen",
                           professor = "Peter Kemper",
                              course = "CSCI 303, Algorithms",
                              rating = total_score,
                              price  = "$" + in_price,
                              link = in_link)

    return render_template("book-info.html",
                                isbn = isbn,
                               title = "Introduction to Algorithms",
                              author = "Thomas H. Cormen",
                           professor = "Peter Kemper",
                              course = "CSCI 303, Algorithms",
                               rating = total_score,
                                price  = "$22.26",
                                link = "https://www.abebooks.com/9780070131439/Introduction-Algorithms-Cormen-Thomas-Leiserson-0070131430/plp")


@nextbook.route("/about")
def about():
    return render_template("about.html")


@nextbook.teardown_appcontext
def teardown_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    nextbook.run(debug = True)
