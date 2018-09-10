from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, TrForm, TranslateForm, AnalyseForm
from translate import Translate
from visual import Visual
from os import getenv


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)


@app.route('/translate', methods=['GET', 'POST'])
def translate():
    form = TrForm()
    if form.validate_on_submit() and form.submit.data:
        return redirect(url_for('translate_words', words=form.text.data))
    elif form.validate_on_submit() and form.submit2.data:
        return redirect(url_for('charts', words=form.text.data))

    return render_template('translate.html', title='Translate', form=form)


@app.route("/to_translate", methods=['GET', 'POST'])
def to_translate():
    form = TranslateForm(request.form)
    if request.method == 'POST':
        if form.validate():
            flash('Text is going to translate')
            return redirect(url_for('translate_words', words=form.text.data))
        else:
            flash('Error: Text to translate is empty')

    return render_template('to_translate.html', form=form)


@app.route("/to_analyse", methods=['GET', 'POST'])
def to_analyse():
    form = AnalyseForm(request.form)
    if request.method == 'POST':
        print(form.text.data)
        if form.validate():
            flash('Text is going to translate')
            return redirect(url_for('charts', words=form.text.data))

        else:
            flash('Error: Text to translate is empty')

    return render_template('to_analyse.html', form=form)

@app.route('/translate_words')
def translate_words():
    translate_server = getenv("TRANSLATE_SRV", "http://127.0.0.1:8080")
    translate = Translate(translate_server)
    words_to_translate = request.args['words']
    count_words = translate.count_words(words_to_translate)
    translate_words = translate.translate_words(count_words)
    words = translate.sort_words(translate_words)

    return render_template('translate_words.html', title='Translated words', words=words)


@app.route('/charts')
def charts():
    translate = Translate()
    words_to_translate = request.args['words']
    count_words = translate.count_words(words_to_translate)
    words = translate.sort_words(count_words)
    visual = Visual(dict_words=words, file_name="line")

    return render_template('chart.html',title='Analysis', chart=visual.mkPie())
