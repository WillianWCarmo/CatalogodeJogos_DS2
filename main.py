from flask import Flask
from controller.index_controller import index_bp
from controller.sobre_controller import sobre_bp
from controller.contato_controller import contato_bp
from controller.jogos_controller import jogos_bp
from controller.detalhes_controller import detalhes_bp

app = Flask(__name__)

# 👇 OBRIGATÓRIO para usar flash()
app.secret_key = "level-up-catalogo-jogos-2025"

app.register_blueprint(index_bp)
app.register_blueprint(sobre_bp)
app.register_blueprint(contato_bp)
app.register_blueprint(jogos_bp)
app.register_blueprint(detalhes_bp)

if __name__ == "__main__":
    app.run(port=9000, debug=True)