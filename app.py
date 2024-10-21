from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Olá Mundo!<h1>"

@app.route("/instagram")
def aluno ():
    return render_template('formulario.html')

@app.route("/envio", nethod=['POST'])
def envioForms():
    nombre=request.form['username']
    passowrd
