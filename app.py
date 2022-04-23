from flask import Flask
from flask import request, render_template, abort, redirect, url_for, \
    make_response
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from AzureDB import AzureDB
from flask_dance.contrib.github import make_github_blueprint, github
from flask_wtf import FlaskForm
from wtforms import StringField, TextField
from email.message import EmailMessage
import secrets
import os
import smtplib


app = Flask(__name__)
mail = Mail(app)

app.secret_key = secrets.token_hex(16)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
github_blueprint = make_github_blueprint(client_id = "c6e6b0697054a23faa43", client_secret = "a6347cac35f0b39b7b732b31deeac6fad8bb1f94",)
app.register_blueprint(github_blueprint, url_prefix = '/login')


@app.route('/email', methods=['POST'])
def send_email():
    email = request.json.get('email', None)

    s = smtplib.SMTP(host='smtp.ethereal.email', port='587')
    s.starttls()
    s.login('wilma.rowe99@ethereal.email', 'RK2zYyqDJJVAwPrPNQ')

    msg = EmailMessage()
    msg.set_content('Witaj przyjacielu !')
    msg['Subject'] = 'Witam Cię bardzo serdecznie!'
    msg['From'] = 'Kacper <kalkowski99@gmail.com>'
    msg['To'] = f'{email}'

    s.send_message(msg)
    s.quit()
    return 'Email sent'


@app.route('/user/<username>', methods=['GET', 'POST'])
@app.route('/', methods=['POST','GET'])

@app.route('/')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            return render_template('index.html', account_info_json = account_info_json)
    return '<h1>Request failed!</h1>'

@app.route('/error_denied')
def error_denied():
    abort(401)

@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505

@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/about")
def about_me():
    return render_template('aboutme.html')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/ksiega")
def ksiega():
    with AzureDB() as a:
        if request.method == 'POST':
            name = request.form.get('Name')
            comment = request.form.get('text')
            data_wpisu = request.form.get('data_wpisu')
            db.azureAddData(name, text)
        data = a.azureGetData()
    return render_template('ksiegagosci', data=data)

@app.route("/process", methods=['POST','GET'])
def process():
    name = request.form['name']
    text = request.form['text']

    with AzureDB() as b:
        b.azureAddData(name,text)
        data = b.azureGetData()
    return render_template('ksiegagosci', data = data, debug=True)

if __name__ == '__main__':
        app.run(debug=True)