from flask import Blueprint, render_template

detalhes_bp = Blueprint("detalhes", __name__)


listaJogos = [

    {
        "id": 1,
        "nome": "Minecraft",
        "descricao": "Jogo de construção e exploração em mundo aberto.",
        "genero": "Sandbox",
        "plataforma": "PC",
        "preco": 99.90,
        "imagem": "/static/imagens/minecraft.webp",
        "sinopse": "Minecraft é um jogo em que o jogador explora um mundo formado por blocos, coleta recursos, constrói estruturas e enfrenta criaturas. O jogador pode criar sua própria aventura, explorar diferentes biomas e sobreviver aos perigos do mundo."
    },

    {
        "id": 2,
        "nome": "GTA V",
        "descricao": "Jogo de ação e aventura em mundo aberto.",
        "genero": "Ação",
        "plataforma": "PC",
        "preco": 79.90,
        "imagem": "/static/imagens/gta.png",
        "sinopse": "Grand Theft Auto V acompanha Michael, Franklin e Trevor, três criminosos com histórias diferentes que acabam envolvidos em grandes assaltos e conflitos. A história se passa em Los Santos, uma cidade aberta onde o jogador pode explorar livremente."
    },

    {
        "id": 3,
        "nome": "FIFA 25",
        "descricao": "Jogo de futebol com diversos times e competições.",
        "genero": "Esporte",
        "plataforma": "PlayStation",
        "preco": 299.90,
        "imagem": "/static/imagens/fifa.png",
        "sinopse": "FIFA 25 é um jogo de futebol que permite aos jogadores disputar partidas, campeonatos e diferentes modos de jogo. É possível controlar clubes e jogadores e participar de competições inspiradas no futebol profissional."
    },

    {
        "id": 4,
        "nome": "God of War",
        "descricao": "Aventura de Kratos e seu filho Atreus pela mitologia nórdica.",
        "genero": "Ação/Aventura",
        "plataforma": "PlayStation",
        "preco": 199.90,
        "imagem": "/static/imagens/gow.jpg",
        "sinopse": "Kratos vive com seu filho Atreus em uma região selvagem da mitologia nórdica. Após a morte da mãe de Atreus, os dois iniciam uma jornada para espalhar suas cinzas no ponto mais alto dos nove reinos. Durante a viagem, enfrentam criaturas e deuses da mitologia nórdica."
    },

    {
        "id": 5,
        "nome": "Hogwarts Legacy",
        "descricao": "RPG de ação e aventura ambientado no mundo mágico de Harry Potter.",
        "genero": "RPG/Aventura",
        "plataforma": "PC, PlayStation, Xbox e Nintendo Switch",
        "preco": 249.90,
        "imagem": "/static/imagens/hogwarts.jpg",
        "sinopse": "Hogwarts Legacy se passa no século XIX, muito antes dos acontecimentos da história de Harry Potter. O jogador assume o papel de um estudante que descobre possuir uma habilidade especial ligada a uma antiga magia. Durante sua jornada, explora Hogwarts, aprende feitiços, participa de aulas e enfrenta ameaças que podem colocar o mundo mágico em perigo."
    },

    {
        "id": 6,
        "nome": "Silksong",
        "descricao": "Aventura de ação e exploração em que Hornet enfrenta novos desafios em um reino misterioso.",
        "genero": "Metroidvania/Ação",
        "plataforma": "PC, Nintendo Switch, PlayStation e Xbox",
        "preco": 69.90,
        "imagem": "/static/imagens/silksong.jpg",
        "sinopse": "Em Hollow Knight: Silksong, Hornet é capturada e levada para um reino misterioso chamado Pharloom. Para descobrir os segredos desse lugar e encontrar uma maneira de escapar, ela precisa enfrentar inimigos, explorar diferentes regiões e dominar novas habilidades."
    },

    {
        "id": 7,
        "nome": "Valorant",
        "descricao": "Jogo de tiro tático em primeira pessoa com agentes que possuem habilidades únicas.",
        "genero": "FPS/Tiro Tático",
        "plataforma": "PC e Console",
        "preco": 0.00,
        "imagem": "/static/imagens/vava.png",
        "sinopse": "Valorant é ambientado em um futuro próximo e acompanha agentes de diferentes partes do mundo. Cada agente possui habilidades próprias e participa de confrontos entre duas equipes. Os jogadores precisam combinar estratégia, habilidades e precisão para vencer as partidas."
    },

    {
        "id": 8,
        "nome": "It Takes Two",
        "descricao": "Jogo cooperativo de aventura em que dois jogadores precisam trabalhar juntos para superar desafios.",
        "genero": "Aventura/Cooperativo",
        "plataforma": "PC, PlayStation e Xbox",
        "preco": 199.90,
        "imagem": "/static/imagens/ittakestwo.jpg",
        "sinopse": "It Takes Two conta a história de Cody e May, um casal que está passando por problemas no relacionamento. Após serem transformados em pequenos bonecos por sua filha, os dois precisam trabalhar juntos para superar diversos desafios e tentar voltar ao normal. Durante a aventura, eles aprendem mais sobre seu relacionamento e sobre a importância de trabalharem juntos."
    }

]


@detalhes_bp.route("/jogo/<int:id>")
def detalhes(id):

    jogoEncontrado = None

    for jogo in listaJogos:

        if jogo["id"] == id:
            jogoEncontrado = jogo

    return render_template(
        "detalhes.html",
        jogo=jogoEncontrado
    )