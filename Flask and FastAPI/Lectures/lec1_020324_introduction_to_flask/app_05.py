from flask import Flask

app = Flask(__name__)

html = """
<p>Вот не думал, не гадал,<br>Программистом взял и
стал.<br>Хитрый знает он язык,<br>Он к другому не привык.</p>
"""


@app.route('/')
def index():
    return 'Hi!'


@app.route('/text/')
def text():
    return html


@app.route('/poems/')
def poems():
    poem = ['Вот не думал, не гадал,',
            'Программистом взял и стал.',
            'Хитрый знает он язык,',
            'Он к другому не привык.',
            ]
    text = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return text


if __name__ == '__main__':
    app.run(debug=True)
