from flask import render_template, flash, redirect, url_for, request, jsonify
from app import db
from app import app
from app.forms import DataForm
from app.models import Data
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    data = Data.query.all()
    return render_template('index.html', title='Home', data=data)


@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    form = DataForm()
    if request.method == 'POST':
        d = Data(altitude=form.altitude.data, longitude=form.longitude.data, latitude=form.latitude.data, airspeed=form.airspeed.data, time=datetime.now())
        db.session.add(d)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('login.html', title='Sign In', form=form)

@app.route('/recent')
def recent():
    data = Data.query.order_by(Data.time.desc()).first()
    return jsonify(altitude = float(data.altitude), longitude = float(data.longitude), latitude = float(data.latitude), airspeed = float(data.airspeed), time = (data.time))
