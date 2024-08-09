from flask import render_template, redirect, url_for, flash
from app import db
from app.forms import SignUpForm
from app.models import User
from flask import current_app as app

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('signup'))
    return render_template('signup.html', form=form)


