from flask import Flask, render_template, request, make_response
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import requests
import os
import pandas as pd
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# API'den verileri çek
url = "https://pomber.github.io/covid19/timeseries.json"
response = requests.get(url)
data = response.json()

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False, default=0)

@app.before_request
def create_tables():
    db.create_all()
    if Visit.query.count() == 0:
        db.session.add(Visit(count=0))
        db.session.commit()

def increase_visit_count():
    visit = Visit.query.first()
    visit.count += 1
    db.session.commit()
    return visit.count

def check_new_visitor():
    visitor_id = request.cookies.get('visitor_id')
    if not visitor_id:
        # Yeni ziyaretçi, sayacı artır ve çerez oluştur
        new_count = increase_visit_count()
        response = make_response(render_template('index.html', countries=countries, dates=dates, visit_count=new_count))
        response.set_cookie('visitor_id', str(uuid.uuid4()), max_age=60*60*24*365*2)  # 2 yıl geçerli
        return response
    else:
        visit_count = Visit.query.first().count
        return render_template('index.html', countries=countries, dates=dates, visit_count=visit_count)

# Ülke ve tarih listesini oluştur
countries = list(data.keys())
dates = sorted([datetime.strptime(entry['date'], '%Y-%m-%d').date() for entry in data['Afghanistan']])

@app.route('/')
def index():
    return check_new_visitor()

@app.route('/result', methods=['POST'])
def result():
    country = request.form['country']
    date = request.form['date']

    # Seçilen ülke verilerini DataFrame'e çevir
    country_data = pd.DataFrame(data[country])

    # Tarih formatını düzelt ve standart hale getir
    country_data['date'] = country_data['date'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d'))

    # Seçilen tarih için veri olup olmadığını kontrol et
    selected_date_data = country_data[country_data['date'] == date]

    if selected_date_data.empty:
        # Eğer veri yoksa, kullanıcıya bir mesaj göster
        error_message = f"Veri bulunamadı: {country} için {date} tarihinde veri mevcut değil."
        return render_template('result.html', country=country, date=date, error_message=error_message)

    # Eğer veri varsa, vaka sayısını al
    case_on_date = selected_date_data['confirmed'].values[0]
    olumSayisi = selected_date_data['deaths'].values[0]
    iyilesmeSayisi = selected_date_data['recovered'].values[0]

    return render_template('result.html', country=country, date=date, cases=case_on_date, olum=olumSayisi, iyiler=iyilesmeSayisi)

if __name__ == '__main__':
    app.run(debug=True)
