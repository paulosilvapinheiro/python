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
    title = 'Here are your results:'
    results = str(search4Vowels(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,
                           )

app.run(debug=True)
