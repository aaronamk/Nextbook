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
    if request.args["filter"] == "professor": # not yet supported
        return render_template("results.html", results="")
    if request.args["filter"] == "class": #not yet supported
        #return redirect(url_for("class_page", title = request.args["q"]))
        return render_template("results.html", results="")

    # covers all other search filters
    results = query_db(f"SELECT * FROM textbook WHERE { request.args['filter'] } LIKE '%{ request.args['q'] }%'")

    return render_template("results.html", results=results)


@nextbook.route("/class-list")
def course_list():
    return render_template("major-directory.html")

    return redirect(url_for("book_page", isbn))

@nextbook.route("/class/<title>", methods = ["GET", "POST"])
def class_page(title):
    #0 = id, 1 = title, 2 = professor, 3 = wiki
    class_info = query_db("select * from course where title = ?", [title])
    if title == "csci303":
        return render_template("class-page.html",
                                title = "CSCI 303 Algorithms",
                                course = "CSCI 303",
                                professor = "Zhenming Liu")
    if len(class_info) > 1:
        return render_template("class-page.html",
                                title = title,
                                course = class_info[0],
                            professor = class_info[2])
    else:
        return render_template("results.html", results="")


@nextbook.route("/review-book")
def review():
    return render_template("review-book.html")

@nextbook.route("/add-book", methods = ["GET", "POST"])
def add_book(isbn = ""):
    if request.method == "POST":
        in_isbn = int(request.form["isbn"])
        in_title = request.form["title"]
        in_author = request.form["author"]
        in_professor = request.form["professor"]
        in_course = request.form["course"]

        try:
            query_db(f"INSERT INTO textbook (isbn, title, author) VALUES ('{in_isbn}','{in_title}','{in_author}');")
            return redirect(url_for("book_page", isbn = in_isbn))
        except:
            return redirect(url_for("book_page", isbn = in_isbn))
    else:
        return render_template("add-book.html", isbn = isbn)


def get_comments(isbn):
    comments = []
    for i in query_db("select * from textbook_comment where isbn = ?", [isbn]):
        #print(i[0],i[1],i[2],i[3], i[4])
        # 0-id, 1 - Username, 2- isbn, 3- Timestamp, 4- Comment
        comments.append([i[1],i[3],i[4]])
    return comments


@nextbook.route("/book/<isbn>", methods = ["GET", "POST"])
def book_page(isbn):
    in_title = "Introduction to Algorithms"
    in_author = "Thomas H Cormen"
    # default titles and authors to

    # if no book with this isbn exists, go to add a book page
    if len(query_db(f"SELECT * FROM textbook WHERE isbn = '{ isbn }'")) == 0:
        return render_template("add-book.html", isbn = isbn)

    count, total_score = 0, 0
    cur_comments = get_comments(isbn)
    for score in query_db("select * from review where isbn = ?", [isbn]):
        count += 1
        total_score += score["score"]
    if (count!=0):
        total_score = round(total_score/count,1)
    for info in query_db("select * from textbook where isbn = ?", [isbn]):
        in_author=info[2]
        in_title=info[1]

    image_file = "default_book_cover.jpg"
    if (isbn=="9780262033848"): # isbn for Algorithms textbook so image displays on screen
        image_file = "Algorithms.jpg"
    elif (isbn == "1118290275"):
        image_file = "data_structs.jpg"
    image = "\static\\" + image_file

    if request.method== "POST":
        in_price = request.form["price"]
        in_link = request.form["link"]
        #TODO interface with database then directly #return redirect(url_for("book_page", isbn = isbn))
        # for now to show price and url changes\
        return render_template("book-info.html",
                                isbn = isbn,
                               title = in_title,
                              author = in_author,
                           professor = "Peter Kemper",
                              course = "CSCI 303, Algorithms",
                              rating = total_score,
                              price  = "$" + in_price,
                                link = in_link,
                              comment= cur_comments,
                              image = image)

    return render_template("book-info.html",
                                isbn = isbn,
                               title = in_title,
                              author = in_author,
                           professor = "Peter Kemper",
                              course = "CSCI 303, Algorithms",
                              rating = total_score,
                              price  = "$22.26",
                            comments = cur_comments,
                                link = "https://www.abebooks.com/9780070131439/Introduction-Algorithms-Cormen-Thomas-Leiserson-0070131430/plp",
                                image = image)


@nextbook.route("/about")
def about():
    return render_template("about.html")

@nextbook.route("/csci")
def csci_page():
    return render_template("com-sci-classes.html")

@nextbook.route("/submit_comment", methods =["POST"])
def submit_comment():
    isbn = int(request.form.get("isbn"))
    rating = int(request.form.get("rating"))
    user = request.form.get("user")
    if (not user or user.isspace()):
        user = "Unknown"
    comment = request.form.get("comment")
    query_db(f"INSERT INTO textbook_comment (isbn, user, body) VALUES ('{isbn}','{user}','{comment}');")
    query_db(f"INSERT INTO review (isbn, score) VALUES ('{isbn}','{rating}');")

    return redirect(url_for("book_page", isbn = isbn))


# TODO: insert into database



@nextbook.teardown_appcontext
def teardown_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    nextbook.run(debug = True)
