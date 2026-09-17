from flask import Blueprint, render_template, request

contato_bp = Blueprint("contato", __name__)


@contato_bp.route("/contato", methods=["GET", "POST"])
def contato():

    dados = ""

    if request.method == "POST":

        nome = request.form.get("nome")
        email = request.form.get("email")
        mensagem = request.form.get("mensagem")

        dados = f"{nome} - {email} - {mensagem}"

    return render_template(
        "contato.html",
        dados=dados
    )