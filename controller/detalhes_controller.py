from flask import Blueprint, render_template

detalhes_bp = Blueprint("detalhes", __name__)


LISTA_JOGOS = [
    {
        "id": 1,
        "nome": "Minecraft",
        "descricao": "Jogo de construção e exploração em mundo aberto.",
        "sinopse": "Minecraft é um jogo sandbox onde você pode explorar mundos infinitos, minerar recursos, construir estruturas e sobreviver a criaturas hostis. Com modos criativo e sobrevivência, oferece liberdade total para criar o que quiser, sozinho ou com amigos.",
        "genero": "Sandbox",
        "plataforma": "PC",
        "preco": 99.90,
        "imagem": "/static/imagens/minecraft.webp",
        "steam": "https://store.steampowered.com/app/1672970/Minecraft/"
    },
    {
        "id": 2,
        "nome": "GTA V",
        "descricao": "Jogo de ação e aventura em mundo aberto.",
        "sinopse": "Grand Theft Auto V acompanha três criminosos — Michael, Franklin e Trevor — em Los Santos, uma cidade inspirada em Los Angeles. Com missões variadas, exploração livre e um modo online massivo, é um dos jogos mais vendidos de todos os tempos.",
        "genero": "Ação",
        "plataforma": "PC",
        "preco": 79.90,
        "imagem": "/static/imagens/gta.png",
        "steam": "https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/"
    },
    {
        "id": 3,
        "nome": "FIFA 25",
        "descricao": "Jogo de futebol com diversos times e competições.",
        "sinopse": "EA Sports FC 25 (antigo FIFA) traz o futebol mais realista da franquia, com times licenciados, modos como Ultimate Team e Carreira, além de gráficos aprimorados e jogabilidade refinada para os fãs do esporte.",
        "genero": "Esporte",
        "plataforma": "PlayStation",
        "preco": 299.90,
        "imagem": "/static/imagens/fifa.png",
        "steam": "https://store.steampowered.com/app/2669320/EA_SPORTS_FC_25/"
    },
    {
        "id": 4,
        "nome": "God of War",
        "descricao": "Aventura de Kratos e seu filho Atreus pela mitologia nórdica.",
        "sinopse": "Após os eventos da mitologia grega, Kratos vive no reino nórdico com seu filho Atreus. Juntos, eles enfrentam deuses, monstros e seus próprios passados em uma jornada épica que mistura ação brutal, exploração e uma história emocionante sobre paternidade.",
        "genero": "Ação/Aventura",
        "plataforma": "PlayStation",
        "preco": 199.90,
        "imagem": "/static/imagens/gow.jpg",
        "steam": "https://store.steampowered.com/app/1593500/God_of_War/"
    },
    {
        "id": 5,
        "nome": "Hogwarts Legacy",
        "descricao": "RPG de ação e aventura ambientado no mundo mágico de Harry Potter.",
        "sinopse": "Ambientado no século XIX, Hogwarts Legacy coloca você como um estudante de Hogwarts com a habilidade rara de manipular magia antiga. Explore o castelo, aprenda feitiços, enfrente criaturas e descubra segredos sombrios do mundo bruxo.",
        "genero": "RPG/Aventura",
        "plataforma": "PC, PlayStation, Xbox e Nintendo Switch",
        "preco": 249.90,
        "imagem": "/static/imagens/hogwarts.jpg",
        "steam": "https://store.steampowered.com/app/990080/Hogwarts_Legacy/"
    },
    {
        "id": 6,
        "nome": "Silksong",
        "descricao": "Aventura de ação e exploração em que Hornet enfrenta novos desafios em um reino misterioso.",
        "sinopse": "Silksong é a sequência de Hollow Knight. Você controla Hornet, explorando um novo reino chamado Pharloom. Com combate mais rápido, novas habilidades e um mundo interconectado, o jogo promete ser um dos maiores metroidvanias da história.",
        "genero": "Metroidvania/Ação",
        "plataforma": "PC, Nintendo Switch, PlayStation e Xbox",
        "preco": 69.90,
        "imagem": "/static/imagens/silksong.jpg",
        "steam": "https://store.steampowered.com/app/1030300/Hollow_Knight_Silksong/"
    },
    {
        "id": 7,
        "nome": "Valorant",
        "descricao": "Jogo de tiro tático em primeira pessoa com agentes que possuem habilidades únicas.",
        "sinopse": "Valorant é um FPS tático 5v5 da Riot Games, onde cada agente tem habilidades únicas. Misturando estratégia, mira precisa e trabalho em equipe, o jogo se tornou um dos maiores eSports do mundo. É gratuito para jogar.",
        "genero": "FPS/Tiro Tático",
        "plataforma": "PC e Console",
        "preco": 0.00,
        "imagem": "/static/imagens/vava.png",
        "steam": ""   # não está na Steam
    },
    {
        "id": 8,
        "nome": "It Takes Two",
        "descricao": "Jogo cooperativo de aventura em que dois jogadores precisam trabalhar juntos para superar desafios.",
        "sinopse": "It Takes Two é um jogo cooperativo obrigatório para dois jogadores. Você controla Cody e May, um casal que virou bonecos após um pedido de divórcio. Juntos, precisam superar desafios criativos em mundos fantásticos para voltarem ao normal.",
        "genero": "Aventura/Cooperativo",
        "plataforma": "PC, PlayStation e Xbox",
        "preco": 199.90,
        "imagem": "/static/imagens/ittakestwo.jpg",
        "steam": "https://store.steampowered.com/app/1426210/It_Takes_Two/"
    }
]


@detalhes_bp.route("/jogo/<int:id>")
def detalhes(id):

    jogoEncontrado = None

    for jogo in LISTA_JOGOS:

        if jogo["id"] == id:
            jogoEncontrado = jogo

    return render_template(
        "detalhes.html",
        jogo=jogoEncontrado
    )