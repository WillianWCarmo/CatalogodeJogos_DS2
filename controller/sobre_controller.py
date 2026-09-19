from flask import Blueprint, render_template

sobre_bp = Blueprint("sobre", __name__)

@sobre_bp.route("/sobre")
def sobre():

    projeto = "Projeto de Catálogo de Jogos"

    exibir = True

    informacoes = "Este site foi desenvolvido para a disciplina de Desenvolvimento para Servidores II."

    lista = ["Flask", "HTML", "CSS", "Python"]

    grupoMembros = [
        {
            "nome": "Willian",
        },

        {
            "nome": "Laura",
        },

        {
            "nome": "Murilo",
        },

        {
            "nome": "Henrique",
        },
    ]

    curso = "Sistemas para Internet"

    return render_template(
        "sobre.html",
        projeto=projeto,
        exibir=exibir,
        lista=lista,
        informacoes=informacoes,
        grupoMembros=grupoMembros,
        curso = curso
    )