from flask import Blueprint, render_template, request, redirect, url_for, flash

contato_bp = Blueprint("contato", __name__)


@contato_bp.route("/contato", methods=["GET", "POST"])
def contato():

    if request.method == "POST":

        # Pega os dados do formulário e remove espaços extras
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        mensagem = request.form.get("mensagem", "").strip()

        # ============================
        # VALIDAÇÕES
        # ============================

        # 1. Campos vazios
        if not nome or not email or not mensagem:
            flash("Por favor, preencha todos os campos antes de enviar.", "erro")
            return redirect(url_for("contato.contato"))

        # 2. Nome muito curto
        if len(nome) < 3:
            flash("O nome deve ter pelo menos 3 caracteres.", "erro")
            return redirect(url_for("contato.contato"))

        # 3. E-mail inválido (verificação simples)
        if "@" not in email or "." not in email.split("@")[-1]:
            flash("Por favor, informe um e-mail válido.", "erro")
            return redirect(url_for("contato.contato"))

        # 4. Mensagem muito curta
        if len(mensagem) < 10:
            flash("A mensagem deve ter pelo menos 10 caracteres.", "erro")
            return redirect(url_for("contato.contato"))

        # ============================
        # SUCESSO
        # ============================

        # Aqui você poderia:
        # - Salvar no banco de dados
        # - Enviar um e-mail
        # - Registrar em um arquivo de log
        # Por enquanto, apenas simulamos o sucesso.

        flash(f"Obrigado, {nome}! Sua mensagem foi enviada com sucesso. 🎮", "sucesso")

        # Redireciona para limpar o formulário (padrão PRG)
        return redirect(url_for("contato.contato"))

    # GET — apenas exibe o formulário
    return render_template("contato.html")