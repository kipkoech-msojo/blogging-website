from flask import Flask, render_template,url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '1b8ab4fce6816adf29e1438f26da19bd'

posts = [
    {
        'author':'collins',
        'title':'football',
        'content':'i love football',
        'date_posted':'nov 2020'
    },
    {
        'author':'kipkoech',
        'title':'coding',
        'content':'i love coding',
        'date_posted':'nov 2020'
    }
]

@app.route('/')
def index():
    title = 'Blogging Website'
    return render_template('index.html',posts=posts,title=title)


@app.route('/register')
def register():
    form = RegistrationForm()
    title = 'Registration form'
    return render_template('register.html',title=title,form=form)

@app.route('/login')
def login():
    form = LoginForm()
    title = 'Login Here'
    return render_template('login.html',form=form,title=title)


if __name__ == '__main__':
    app.run(debug=True)