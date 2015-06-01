from flask import Flask
from flask import render_template
from forms import WineForm

app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/')
def home():
    form = WineForm()
    return render_template('main.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
