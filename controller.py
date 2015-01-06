from flask import request, render_template, session
from flask.ext.sqlalchemy import SQLAlchemy

from __init__ import app

db= SQLAlchemy(app)
	
from models import *

@app.route('/')
def hello_world():
   return render_template('1.html')

@app.route('/minigame')
def mini_game():
	return render_template('ho.html')

@app.route('/webart')
def web_art():
	return render_template('webart.html')

@app.route('/star')
def star():
	import urllib
	from bs4 import BeautifulSoup
	url=urllib.urlopen('http://image.search.naver.com/search.naver?where=image&sm=tab_jum&ie=utf8&query=%EC%88%98%EC%A7%80')
	soup=BeautifulSoup(url)
	return render_template('star.html',soup=soup)

@app.route('/program')
def p_rogramming():
	return render_template('home.html')

@app.route('/my')
def my_page():
	return render_template('my.html')

@app.route('/media')
def media():
	import urllib
	from bs4 import BeautifulSoup
	url1=urllib.urlopen('http://besuccess.com/')
	url2=urllib.urlopen('http://platum.kr/')
	url3=urllib.urlopen('http://www.venturesquare.net/')
	url4=urllib.urlopen('http://www.youtube.com/')
	soup1=BeautifulSoup(url1)
	soup2=BeautifulSoup(url2)
	soup3=BeautifulSoup(url3)
	soup4=BeautifulSoup(url4)
	return render_template('2.html',soup1=soup1,soup2=soup2,soup3=soup3,soup4=soup4)

@app.route('/souptest')
def souptest():
	import urllib
	from bs4 import BeautifulSoup
	url=urllib.urlopen('http://finance.naver.com/recommendationItem/')
	soup=BeautifulSoup(url)
	return render_template('3.html',soup=soup)

@app.route('/memo')
def b_memo():
	return render_template('ho2.html')

@app.route('/login', methods=['POST'])
def login():
	user_id=request.form['user_id']
	user_pw=request.form['user_pw']
	if user_id== 'tkdduq500':
		if user_pw=='sy1120':
			session['logged_in']=True
			return render_template('ho2.html')
		else:
			return 'wrong password'
	else:
		return 'wrong id'