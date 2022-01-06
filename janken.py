from bottle import request, run, get, route, template, TEMPLATE_PATH, static_file
import os
import random
#ローカル環境のフォルダパスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
VIEWS_DIR = os.path.join(BASE_DIR, 'views')
TEMPLATE_PATH.insert(0, VIEWS_DIR)


@route("/")
def index():
    return template()

@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root=f"{STATIC_DIR}\css")

@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root=f"{STATIC_DIR}\img")

run(host='localhost', port=8080, debug=True) 
