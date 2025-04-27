from jogoteca import app, db
from flask import render_template, request, redirect, session, flash, url_for
from models import usuarios
from helpers import FormularioUsuario,FormularioAlterarSenha, FormularioNovoUsuario
from flask_bcrypt import check_password_hash, generate_password_hash

@app.route('/')
def login():
    form=FormularioUsuario()

    proxima = request.args.get('proxima')
    if proxima is None:
        proxima = '/lista'
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form=FormularioUsuario(request.form)

    usuario = usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario logado'] = usuario.nickname
        user_logged = session['usuario logado']
        flash(usuario.nickname + ' logado')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('usuario não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario logado'] = None
    flash('Logout feito')
    return redirect(url_for('login'))

@app.route('/alterarsenha')
def alterarsenha():
    if 'usuario logado' not in session or session['usuario logado'] == None:
        return redirect(url_for('login', proxima=url_for('alterarsenha')))
    
    form=FormularioAlterarSenha()

    nickname = session['usuario logado']

    form.nickname.data = nickname

    proxima = request.args.get('proxima')
    return render_template('alterarsenha.html', proxima=proxima, form=form)

@app.route('/alterasenha', methods=['POST',])
def alterasenha():
    form=FormularioAlterarSenha(request.form)
    nickname = session['usuario logado']
    if form.validate_on_submit():
        usuario = usuarios.query.filter_by(nickname=nickname).first()
        usuario.senha = generate_password_hash(form.senha.data).decode('utf-8') 
        
        db.session.add(usuario)
        db.session.commit()

        flash('Senha alterada')
        return redirect(url_for('lista'))
    else:
        flash('usuario não logado')
        return redirect(url_for('login'))
    
@app.route('/novousuario')
def novousuario():
    if 'usuario logado' not in session or session['usuario logado'] == None:
        return redirect(url_for('login', proxima=url_for('novousuario')))
    form = FormularioNovoUsuario()
    return render_template('novousuario.html', titulo='Novo', form=form)

@app.route('/criarusuario', methods=['POST',])
def criarusuario():
    form = FormularioNovoUsuario(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('novousuario'))

    nome = form.nome.data
    nickname = form.nickname.data
    senha = generate_password_hash(form.senha.data).decode('utf-8') 
    
    usuario = usuarios.query.filter_by(nickname=nickname).first()

    if usuario:
        flash('Nickname já existe')
        return redirect(url_for('novousuario'))

    novo_usuario = usuarios(nome=nome,nickname=nickname,senha=senha)
    db.session.add(novo_usuario)
    db.session.commit()
    return redirect(url_for('lista'))