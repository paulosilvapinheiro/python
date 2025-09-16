# from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request
from vsearch import search4Vowels

app = Flask(__name__)


# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')


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

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title="Welcome to search4Letters onde web!")

if __name__ == '__main__':
    app.run(debug=True)
