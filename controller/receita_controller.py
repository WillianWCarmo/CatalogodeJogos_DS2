from flask import Blueprint, render_template, request

receita_bp = Blueprint("receita", __name__)

@receita_bp.route("/receita/cadastrar", methods=["GET", "POST"])
def cadastrar():
    return render_template("receita_cadastro.html")