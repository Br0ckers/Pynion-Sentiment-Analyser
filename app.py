#! /usr/bin/env python
from flask import request, jsonify, Flask, flash, redirect, render_template, session, abort, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField 
from app import app,twittclient

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
        # flash('Your Subject is ' + subject)
        getOp(subject)
        return redirect('pynion')
    else:
        flash('To see what the twitterverse current opinion is, on a topic, enter it below')
        return render_template('index.html', form=form)

def getOp(subject):
    ptwee = []
    ntwee = []
    # creating object of TwitterClient Class
    api = twittclient.TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = subject, count = 20)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    session['pos'] = "Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    session['neg'] = "Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} % \
         ".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
    session['nue'] = "Neutral tweets percentage: {} % ".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets))

    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])
        ptwee.append(tweet['text'])
    session['ptweet'] = tuple(ptwee)

    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
        ntwee.append(tweet['text'])
    session['ntweet'] = tuple(ntwee)

@app.route("/pynion")
def pynion_matter():
    return render_template('pynion.html')

@app.route("/result")
def test():
    return render_template(
        'result.html')

@app.route("/test")
def test2():
    return render_template(
        'test.html')

if __name__ == "__main__":
    app.run('0.0.0.0',5000,ssl_context=('/Users/phipax/cert/ssl.crt', '/Users/phipax/cert/ssl.key'))
