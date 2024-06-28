from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/produk")
def produk():
    return render_template("produk.html")


@app.route("/pesan")
def  pesan():
    return render_template("pesan.html")

@app.route("/transaksi")
def transaksi():
    return render_template("transaksi.html")

