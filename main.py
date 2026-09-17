from flask import Flask
from controller.index_controller import index_bp
from controller.sobre_controller import sobre_bp
from controller.contato_controller import contato_bp
from controller.jogos_controller import jogos_bp
from controller.detalhes_controller import detalhes_bp

# from controller.receita_controller import receita_bp
# from database import Base, engine

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(sobre_bp)
app.register_blueprint(contato_bp)
app.register_blueprint(jogos_bp)
app.register_blueprint(detalhes_bp)

if __name__ == "__main__":
    app.run(port=9000, debug=True)