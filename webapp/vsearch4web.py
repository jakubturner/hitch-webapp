from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase=phrase, letters=letters))
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def render_entry() -> "html":
    return render_template('entry.html', the_title='Welcome to entry page')


if __name__ == '__main__':
    app.run(debug=True)
