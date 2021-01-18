# zadaća 15 - My homepage

from flask import Flask, render_template

app = Flask(__name__)

# kontroler index
@app.route("/")
def index():
    return render_template("index.html")

# kontroler about
@app.route("/about")
def about():
    return render_template("about.html")

# kontroler portfolio
@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

# kontroler portfolio/fakebook
@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")

# kontroler portfolio/boogle
@app.route("/portfolio/boogle")
def boogle():
    return render_template("boogle.html")

# kontroler portfolio/hair-salon
@app.route("/portfolio/hair-salon")
def salon():
    return render_template("hair-salon.html")

# kontroler portfolio/fakebook/profil
@app.route("/portfolio/fakebook/profil")
def profil():
    return render_template("profil.html")

if __name__ == '__main__':
    app.run()