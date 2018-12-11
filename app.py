from flask import request, jsonify, Flask, flash, redirect, render_template, session, abort, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Subject:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ReusableForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        subject=request.form['name']
        print (subject)

    if form.validate():
# Save the comment here.
        flash('Your Subject is ' + subject)
    else:
        flash('Enter your message subject. ')


    return render_template(
        'index.html', form=form)

@app.route("/test")
def test():
    return render_template(
        'test.html')

if __name__ == "__main__":
    app.run()
