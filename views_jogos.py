from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app, db
from models import jogos, CLIENTE, TELEFONE
from helpers import FormularioJogo

@app.route('/lista')
def lista():
    if 'usuario logado' not in session or session['usuario logado'] == None:
        return redirect(url_for('login', proxima=url_for('lista')))
    lista = jogos.query.order_by(jogos.id)
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route("/search")
def search():
    q = request.args.get("q")
    if q:
        results = jogos.query.filter(jogos.nome.icontains(q)).order_by(jogos.id).limit(100).all()
    else:
        results = jogos.query.order_by(jogos.id).limit(100).all()
    return render_template("search_results.html", results=results)

@app.route('/novo')
def novo():
    if 'usuario logado' not in session or session['usuario logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioJogo()
    return render_template('novo.html', titulo='Novo', form=form)

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario logado' not in session or session['usuario logado'] == None:
        return redirect(url_for('login'))
    jogo = jogos.query.filter_by(id=id).first()

    form=FormularioJogo()

    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console

    return render_template('editar.html', titulo='Editando', id=id, form=form)

@app.route('/criar', methods=['POST',])
def criar():
    form = FormularioJogo(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('novo'))

    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data
    
    jogo = jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash('Jogo existe')
        return redirect(url_for('lista'))    

    novo_jogo = jogos(nome=nome,categoria=categoria,console=console)
    db.session.add(novo_jogo)
    db.session.commit()
    return redirect(url_for('lista'))

@app.route('/atualizar', methods=['POST',])
def atualizar():
    form = FormularioJogo(request.form)

    if form.validate_on_submit():
        jogo = jogos.query.filter_by(id=request.form['id']).first()
        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data

        db.session.add(jogo)
        db.session.commit()

    return redirect(url_for('lista'))

@app.route('/excluir/<int:id>')
def excluir(id):
    if 'usuario logado' not in session or session['usuario logado'] == None:
        return redirect(url_for('login'))
    
    jogos.query.filter_by(id=id).delete()

    db.session.commit()
    flash('jogo deletado')
    return redirect(url_for('lista'))

