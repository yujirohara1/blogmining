from flask import Flask, render_template, g, request, redirect, url_for, Response, abort, session, jsonify, make_response, send_file
from hamlish_jinja import HamlishExtension
from werkzeug.datastructures import ImmutableDict
import os
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from collections import defaultdict
from datetime import timedelta
import datetime
from flask_bootstrap import Bootstrap
import json
import csv
import requests
from bs4 import BeautifulSoup
import collections
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud


class FlaskWithHamlish(Flask):
    jinja_options = ImmutableDict(
        extensions=[HamlishExtension]
    )
app = FlaskWithHamlish(__name__)
bootstrap = Bootstrap(app)

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

@app.route('/tryScrapeKiji/<kijiId>')
def tryScrapeKiji(kijiId):
  # スクレイピング対象の URL にリクエストを送り HTML を取得する
  # res = requests.get('https://www.njss.info/bidders/view/' + vendornm + '/')

  dictJuchu = {}
  dictJuchu['aaData']=[]
  # kijiId = 200
  # while kijiId < 220:
  res = requests.get('http://kiyonagi.jp/?p=' + str(kijiId))
  # レスポンスの HTML から BeautifulSoup オブジェクトを作る
  soup = BeautifulSoup(res.text, 'html.parser')
  # title タグの文字列を取得する
  
  # soup.select('article') 

  if soup.find(class_="post-full post-full-summary") is not None:
    title_text = soup.find(class_='entry-title').get_text()
    body_text = soup.find(class_='entry-content').get_text()
    cate_text = soup.find(class_='cat-links').get_text()
    date_text = ""
    if soup.find(class_='entry-date') is not None:
      date_text = formatDate(soup.find(class_='entry-date').get_text())

    # 文字の整形（改行削除）
    text = "".join(body_text.splitlines())

    # 単語ごとに抽出
    docs=[]
    t = Tokenizer()
    tokens = t.tokenize(text)
    for token in tokens:
        if len(token.base_form) > 2:
            docs.append(token.surface)
    
    c_word = ' '.join(docs)
    
    filepath = ''
    filename = ''
    if c_word != '':
      wordcloud = WordCloud(background_color='white',
                          font_path='NotoSansJP-Regular.otf',
                          width=800, height=400).generate(c_word)
      ## 結果を画像に保存
      timestamp = datetime.datetime.now()
      timestampStr = timestamp.strftime('%Y%m%d%H%M%S%f')
      filename = "wordcloud_" + timestampStr + "_" + kijiId + ".png"
      filepath = "./static/image/" + filename
      wordcloud.to_file(filepath)

    dictJuchu["aaData"].append( \
      {"id":kijiId, \
        "title":title_text.replace("\n",""), \
        "kaiseki": c_word, \
          "filepath": filename, \
          "category": cate_text.replace("\n",""), \
            "tokoDate": date_text, \
              "honbun": body_text.replace("\n","")} 
        )
  # kijiId+=1

  return json.dumps(dictJuchu, skipkeys=True, ensure_ascii=False)

def formatDate(dateText):
  ret = dateText.replace("年","/")
  ret = ret.replace("月","/")
  ret = ret.replace("日","")
  vals = ret.split("/")
  vals[1] = ("0" + vals[1])[-2:]
  vals[2] = ("0" + vals[2])[-2:]
  ret = vals[0] + "年" +  vals[1] + "月" +  vals[2] + "日"
  
  return ret



# ログインパス
@app.route('/', methods=["GET", "POST"])
def login():
  return render_template('index.haml')


if __name__ == "__main__":
    app.run(debug=True)
