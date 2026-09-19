from flask import Blueprint, render_template
from controller.jogos_controller import LISTA_JOGOS

index_bp = Blueprint("index", __name__)   # 👈 renomeado


@index_bp.route("/")
def index():
    destaques = LISTA_JOGOS[:4]
    return render_template("index.html", jogos=destaques)