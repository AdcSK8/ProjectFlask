# coding:utf-8

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask("projeto")

app.secret_key = "awdUJHudhuawdbnacbauwdbasbcj"


@app.route("/")
def ola_mundo():
     nome="Andre Dias"
     produtos = [
          {"nome": "Ração", "preco": 199.99},
          {"nome": "Playstation", "preco": 1999.99}]

     return render_template("alo.html", n=nome, aProdutos=produtos), 200

#NOVA ROTA
@app.route("/teste")
@app.route("/teste/<variavel>")
def funcao_teste(variavel = ""):
     return "Nova rota teste<br>Variável: {}".format(variavel), 200

#ROTA FORMULARIO
@app.route("/form")
def form():
     return render_template("form.html"), 200

#ROTA TRATAMENTO FORMULARIO
@app.route("/form_recebe", methods=["POST", "GET"])
def form_recebe():
     nome = ""
     if request.method == "POST":
          nome = request.form["nome"]
     return "Nome: {}".format(nome)   

#ROTA FORM DE LOGIN
@app.route("/login")
def login():
     return render_template("login.html"), 200

#ROTA PARA VALIDAR O FORMULARIO
@app.route("/login_validar", methods=["POST"])
def login_validar():
     if request.form["usuario"] == "admin" and request.form["senha"] == "123":
          session["usuario"] = request.form["usuario"]
          session["codigo"] = 1
          return redirect(url_for("acesso_restrito"))
     else:
          return "Usuario/Senha inválidos, digite novamente.", 200

#ROTA PARA AREA RESTRITA
@app.route("/restrito")
def acesso_restrito():
     if session["codigo"] == 1:
          return "Bem_vindo à area restrita!<br>Usuário: {}<br>Código:{}.".format(session["usuario"], session["codigo"]), 200
     else:
          return "Acesso inválido", 200

app.run()