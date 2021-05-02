from flask import Flask, render_template
from helium import *
from selenium import webdriver
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/moogsoft")
def moogsoft():
    moogsoft.driver = start_chrome()


@app.route("/google")
def google():
    moogsoft.driver.execute_script("window.open('');")
    go_to('www.google.com')
    click("I'm Feeling Lucky")

if __name__ == "__main__":
    app.run(debug=True)
