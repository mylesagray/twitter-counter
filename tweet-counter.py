import os
from TwitterAPI import TwitterAPI
from flask import Flask, render_template, request
app = Flask(__name__)

# Env vars
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# Twitter API querying          
api = TwitterAPI(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Flask webapp
@app.route("/")
def main():
	return render_template('index.html')

@app.route('/count/<some_query>')
def tweets_page(some_query):
	r = api.request('search/tweets', {'q':some_query})
	count = 0
	for item in r:
		count += 1
	return render_template('count.html', tweet = some_query, tweet_count = count)

if __name__ == "__main__":
    app.run(host= '0.0.0.0')