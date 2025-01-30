from flask import Flask, render_template, request
from vsearch import search4Vowels

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello workd from Flask'


@app.route('/search4', methods=['GET', 'POST'])
def do_search() -> str:
    phrase = request.form['Phrase']
    letters = request.form['Letters']
    return str(search4Vowels(phrase, letters))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title="Welcome to search4Letters onde web!")


def result_do_search_page(phrase: str, letters: str, result: str) -> 'html':
    return render_template('results.html'
                           ,the_title = "Retorno do formulário!")

app.run(debug=True)
