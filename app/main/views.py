from flask import render_template, redirect, url_for, flash
from .forms import NameForm
from ..models import User, Role
from .. import db
from datetime import datetime
from . import main


@main.route('/')
def index():
    return render_template('index.html',current_time=datetime.now())


@main.route('/professores', methods=['GET', 'POST'])
def professores():
    form = NameForm()

    disciplines = ['DSWA5','IHCA5','SODA5','PJIA5','GPSA5', 'TCOA5']

    roles = Role.query.filter( Role.name.in_(disciplines)).order_by(Role.name).all()

    form.role.choices = [(role.name, role.name) for role in roles]

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()

        if user is None:
            role = Role.query.filter_by(name=form.role.data ).first()

            user = User(username=form.name.data,role=role)

            db.session.add(user)
            db.session.commit()

            flash('Professor cadastrado com sucesso!')
        else:
            flash('Este professor já está cadastrado.')

        return redirect(url_for('main.professores'))

    role_ids = [role.id for role in roles]

    user_all = User.query.filter(User.role_id.in_(role_ids)).order_by(User.username).all()

    return render_template(
        'cadastros/professores.html',form=form, user_all=user_all)



@main.route('/disciplinas')
def disciplinas():
    return render_template('cadastros/placeholder.html', current_time=datetime.now())


@main.route('/alunos')
def alunos():
    return render_template('cadastros/placeholder.html',current_time=datetime.now())


@main.route('/cursos')
def cursos():
    return render_template('cadastros/placeholder.html', current_time=datetime.now())


@main.route('/ocorrencias')
def ocorrencias():
    return render_template('cadastros/placeholder.html', current_time=datetime.now())
