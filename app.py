from flask import Flask, render_template, g, request, redirect, url_for, Response, abort, session, jsonify, make_response, send_file
from hamlish_jinja import HamlishExtension
from werkzeug.datastructures import ImmutableDict
import os
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from collections import defaultdict
from datetime import timedelta
import datetime
from flask_bootstrap import Bootstrap
from marshmallow_sqlalchemy import ModelSchema
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4, portrait
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from api.database import db, ma
from models.item import Item, ItemSchema, VItemGroup, VItemGroupSchema
from models.customer import Customer, CustomerSchema, CustomerNentuki, CustomerNentukiSchema
from models.mstsetting import MstSetting, MstSettingSchema
from models.daicho import Daicho, DaichoSchema, VDaichoA, VDaichoASchema
from models.seikyu import Seikyu, SeikyuSchema, VSeikyuA, VSeikyuASchema, VSeikyuB, VSeikyuBSchema, VSeikyuC, VSeikyuCSchema
# from models.toko import Toko, TokoSchema, 
# from models.tokoradar import TokoRadar, TokoRadarSchema, VTokoRadarGroupByVendor, VTokoRadarGroupByVendorSchema
# from models.bunya import Bunya, BunyaSchema
from models.kaito import Kaito, KaitoSchema, VTokoGroupbyVendor, VTokoGroupbyVendorSchema, VTokoGroupbySystem, VTokoGroupbySystemSchema, VTokoRadarGroupByVendor, VTokoRadarGroupByVendorSchema, VBunyaMapGroupbyVendor, VBunyaMapGroupbyVendorSchema, VTodohukenGroupbyVendor, VTodohukenGroupbyVendorSchema
from sqlalchemy.sql import text
from sqlalchemy import distinct
from sqlalchemy import desc
from sqlalchemy import asc
import json
# from rq import Queue
# from worker import conn
import PyPDF2
# from bottle import route, run
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import csv
import requests
from bs4 import BeautifulSoup


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

    dictJuchu["aaData"].append( \
      {"id":kijiId, \
        "title":title_text.replace("\n",""), \
        "todofuken": "aaa", \
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
