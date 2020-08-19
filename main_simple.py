from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/adultos")
def adultos():
    return render_template("adultos.html")

@app.route("/niños")
def niños():
    return render_template("niños.html")

@app.route("/babyshower")
def babyshower():
    return render_template("babyshower.html")

if __name__ == "__main__":
    app.run(debug=True)