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
    return " | ".join(f"{k}: {v}" for k, v in request.args.items())


@nextbook.route("/class-list")
def class_list():
    return "full list"




@nextbook.route("/add-book", methods = ['GET', 'POST'])
def add_book():
    if request.method == "POST":
            print("here")
            title = quote_plus(request.form["title"])
            author = quote_plus(request.form["author"])
            isbn = quote_plus(request.form["isbn"])
            professor = quote_plus(request.form["professor"])
            Class = quote_plus(request.form["Class"])
            print(isbn)
            return redirect(f"added-book?title={title}&author={author}&isbn={isbn}&professor={professor}&Class={Class}")
    else:
        return render_template("AddBook.html")
@nextbook.route("/added-book")
def book_results():
    return "Thanks, " + request.args.get("title")+ " by " + request.args.get("author") + " has been added to our book list!"


@nextbook.route("/about")
def about():
    return "We are cool bros!"


if __name__ == "__main__":
    nextbook.run(debug = True)
