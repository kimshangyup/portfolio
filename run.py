from __init__ import app

if __name__ == '__main__':
	app.secret_key='asdfasdf'
	app.run(debug=True, host='0.0.0.0')