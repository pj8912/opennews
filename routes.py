from flask import request, redirect, make_response, url_for, render_template, flash
from main import app
import sys
from db_config import conn, cursor
import sqlite3
from constants import * 


sys.path.append(MODELS_ROUTE)
from language import Language
lang_ = Language(conn, cursor)



# home feed
@app.route('/')
def home():
    return render_template('index.html')



# settings page
# add/update/remove rss links
@app.route("/settings")
def settings():
    return render_template('settings.html')


# view saved news
@app.route('/savednews')
def savedNews():
    return render_template('saved_news.html')


# upload new language to database
@app.route('/addlanguage', methods=['POST'])
def addLanguage():
    if request.method == "POST":
        lang = request.form['language']
        if lang == '':
            flash("Lanuage is empty!", "error")
            return redirect('/settings')
        try:
            lang_.create(lang)
            flash("Lanuage uploaded successfully!", "success")
            return redirect('/settings')
        except sqlite3.Error as e:
            return "DB Error:"+str(e)
    else:
        flash("Wrong method", "error")
        return redirect('/')

