from flask import Blueprint, render_template

jogos_bp = Blueprint("jogos", __name__)


@jogos_bp.route("/jogos")
def jogos():

    listaJogos = [
        {
            "id": 1,
            "nome": "Minecraft",
            "descricao": "Jogo de construção e exploração em mundo aberto.",
            "genero": "Sandbox",
            "plataforma": "PC",
            "preco": 99.90,
            "imagem": "/static/imagens/minecraft.webp"
        },

        {
            "id": 2,
            "nome": "GTA V",
            "descricao": "Jogo de ação e aventura em mundo aberto.",
            "genero": "Ação",
            "plataforma": "PC",
            "preco": 79.90,
            "imagem": "/static/imagens/gta.png"
        },

        {
            "id": 3,
            "nome": "FIFA 25",
            "descricao": "Jogo de futebol com diversos times e competições.",
            "genero": "Esporte",
            "plataforma": "PlayStation",
            "preco": 299.90,
            "imagem": "/static/imagens/fifa.png"
        },

        {
            "id": 4,
            "nome": "God of War",
            "descricao": "Aventura de Kratos e seu filho Atreus pela mitologia nórdica.",
            "genero": "Ação/Aventura",
            "plataforma": "PlayStation",
            "preco": 199.90,
            "imagem": "/static/imagens/gow.jpg"
        },

        {
            "id": 5,
            "nome": "Hogwarts Legacy",
            "descricao": "RPG de ação e aventura ambientado no mundo mágico de Harry Potter.",
            "genero": "RPG/Aventura",
            "plataforma": "PC, PlayStation, Xbox e Nintendo Switch",
            "preco": 249.90,
            "imagem": "/static/imagens/hogwarts.jpg"
        },

        {
            "id": 6,
            "nome": "Silksong",
            "descricao": "Aventura de ação e exploração em que Hornet enfrenta novos desafios em um reino misterioso.",
            "genero": "Metroidvania/Ação",
            "plataforma": "PC, Nintendo Switch, PlayStation e Xbox",
            "preco": 69.90,
            "imagem": "/static/imagens/silksong.jpg"
        },

        {
            "id": 7,
            "nome": "Valorant",
            "descricao": "Jogo de tiro tático em primeira pessoa com agentes que possuem habilidades únicas.",
            "genero": "FPS/Tiro Tático",
            "plataforma": "PC e Console",
            "preco": 0.00,
            "imagem": "/static/imagens/vava.png"
        },

        {
            "id": 8,
            "nome": "It Takes Two",
            "descricao": "Jogo cooperativo de aventura em que dois jogadores precisam trabalhar juntos para superar desafios.",
            "genero": "Aventura/Cooperativo",
            "plataforma": "PC, PlayStation e Xbox",
            "preco": 199.90,
            "imagem": "/static/imagens/ittakestwo.jpg"
        }
]

    return render_template(
        "jogos.html",
        jogos=listaJogos
    )