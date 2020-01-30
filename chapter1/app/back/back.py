from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy import exc
import json
from random import randint
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@data:3306/mydatabase'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
#app.secret_key = 'changethis'

@app.route('/api/v1/get-quote', methods=['GET'])
def get_quote():
    # Get the number of quotes saved in out DB
    length_query = text('SELECT COUNT(id) FROM quotes')
    length_result = db.engine.execute(length_query)
    length = length_result.fetchone()[0]
    # Return a random integer random_id where: 1 < random_id < length
    random_id = randint(1, int(length))
    # Selecting a random quote using a random quote id
    sql = text('select quote from quotes where id=%s' % (random_id) )
    result = db.engine.execute(sql)
    # Returning the quote
    random_quote = result.first()[0]
    return json.dumps({'random_quote':random_quote}), 200, {'ContentType':'application/json'}

@app.route('/api/v1/set-quote', methods=['POST'])
def set_quote():
    # Reading the POST JSON data using the key "quote"
    quote = request.json['quote']
    # Inserting the quote in the database
    sql = text('INSERT INTO quotes (quote) VALUES ("%s");' % quote)
    # This will return a success message if the quote is inserted otherwise it wil return a 500 server error
    try:
        result = db.engine.execute(sql)
    except exc.IntegrityError:
        return json.dumps({'success':False}), 500, {'ContentType':'application/json'}
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route('/healthz', methods=['GET'])
def healthz():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return json.dumps({'up':True}), 200, {'ContentType':'application/json'}
    except:
        return json.dumps({'up':False}), 500, {'ContentType':'application/json'}


# This API will run on port 3000 on host 0.0.0.0.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
