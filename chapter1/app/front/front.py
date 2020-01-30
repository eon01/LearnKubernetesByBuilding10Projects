from flask import Flask, flash, redirect, render_template, request, session, abort
import requests, json

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    r = requests.get('http://api:3000/api/v1/get-quote')
    q = json.loads(r.text)
    q = q['random_quote']
    return render_template('index.html', quote = q, name = name)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001, debug=True)
