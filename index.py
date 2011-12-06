from flask import Flask, render_template, g, redirect, url_for
import sqlite3

#configuration -- need to move to separate file
DATABASE = '/tmp/urls.db' 
DEBUG = True

app = Flask(__name__)

@app.route('/')
@app.route('/<shortUrl>')
def index(shortUrl = ''):
	print(shortUrl)
	if shortUrl == '':
		return 'Url Shortner'
	else:
		#response redirect to long Url in DB
		cur = g.db.execute('select longUrl from urls where shortUrl=?',shortUrl)
		row = cur.fetchone()
		if row == None:
			return redirect(url_for('index'))
		return redirect(row[0], 302)

def connect_db():
	return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	g.db.close()

if __name__ == '__main__':
	app.run(debug=DEBUG)

