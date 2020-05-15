from flask import Flask
from flask import render_template
from flask import redirect, url_for, request

app = Flask(__name__)

article_dict = {1:{"title":"My first article",
                    "content":"Hello! This is my first article. Just testin Flask"},
                2:{"title":"My Second Article",
                    "content":"This is my second article. Should be better than the first"},
                3:{"title":"My last Article",
                    "content":"This is my third article. Nothing to say anymore"}}


@app.route("/")
def home():
    return render_template("home.html", article_dict = article_dict)


@app.route("/article/<int:article_num>")
def article_page(article_num):

    # article = article_dict[article_num]
    article = article_dict.get(article_num, None)
    return render_template("article.html", article = article)


@app.route("/write", methods=["GET","POST"])
def write():
    if request.method == "POST":
        print(request.form)
        article_num = max(list(article_dict.keys())) + 1
        article_title = request.form["title"]
        article_content = request.form["content"]
        article_dict[article_num] = {"title":article_title, "content":article_content}
        return redirect(url_for("home"))
    else:
        return render_template("write.html")


if __name__ == "__main__":
    app.run(debug = True)