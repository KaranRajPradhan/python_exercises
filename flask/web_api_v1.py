from flask import Flask, jsonify
import metaweather_wrapper

app = Flask(__name__)

article_dict = {1:{"title":"My first article",
                    "content":"Hello! This is my first article. Just testin Flask"},
                2:{"title":"My Second Article",
                    "content":"This is my second article. Should be better than the first"},
                3:{"title":"My last Article",
                    "content":"This is my third article. Nothing to say anymore"}}

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route("/bye")
def bye():
    return "bye bye!"

@app.route("/weather")
def weather():
    six_days_weather_list = metaweather_wrapper.main()
    return jsonify(six_days_weather_list)

@app.route("/article/<int:article_num>")
def web_page(article_num):

    # article = article_dict[article_num]
    article = article_dict.get(article_num, "Not found")
    return f"""
            <html>
                <body>
                    <h1> {article["title"]} </h1>
                    <p> {article["content"]} </p></br>
                    <a href='http://localhost:5000'>Home</a>
                </body>
            </html>
            """

@app.route("/")
def home():
    article_list = []
    for key in article_dict.keys():
        article_url = f"<a href='http://localhost:5000/article/{key}'>{article_dict[key]['title']}</a></br>"
        article_list.append(article_url)
    article_html_list = "\n".join(article_list)
    return f"<html><body><h1> {article_html_list} </h1></body></html>"


if __name__ == "__main__":
    app.run(debug = True)