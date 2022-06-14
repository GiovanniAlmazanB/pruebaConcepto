from flask import Flask, render_template, request, redirect, url_for, g
import psycopg2
from psycopg2 import pool
import os

#Sintaxis de Flask, no mover esta línea de código.
app = Flask(__name__)
#conexión a la base de datos.

#Ruta del Index o Pantalla de Home.
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pie")
def pie():
    return render_template("pie.html")

@app.route("/line")
def line():
    return render_template("line.html")

@app.route("/pie2", methods=["GET", "POST"])
def pieCopy():
    
    return render_template("pie2.html")
#Ruta que carga la pantalla de estadísticas, adémas del llenado de los selectfield.

@app.route("/recibirData", methods=["GET", "POST"])
def data():
    unidad1 = request.args.get('unidad1')
    sector1 = request.args.get('sector1')
    departamento1 = request.args.get('departamento1')
    areainv1 = request.args.get('areainv1')
    return

#Condicional para el funcionamiento de Flask, no tocar.
if __name__=="__main__":
    app.run(debug=True)
