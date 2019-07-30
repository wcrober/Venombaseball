from flask import render_template, url_for, flash, redirect
from venom import app
from venom.forms import RegistrationForm, LoginForm
from venom.models import User, Post



posts = [
    {
         'author': 'Keyshawn Reed',
         'title': '2019 Team Tryouts',
         'content': 'We will be having open tryouts at Fall Creek Baseball Fields',
         'date_posted': 'July 24, 2019'
    },
    {
         'author': 'Keyshawn Reed',
         'title': '2019 World Series Banquet Fundraiser',
         'content': 'The team will be hosting a dinner in support of our boys going to Florida to play in the 2019 World Series',
         'date_posted': 'July 22, 2019'
    },


]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/blog')
def blog():
    return render_template('blog.html', title='Blog', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)