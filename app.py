from client import *
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    data = get_updated_data()

    JSONResponse = {
        "ok":True,
        "data":data,
        "message":"Sukses"
    }
    return jsonify(JSONResponse)

@app.route('/yearly', methods=['GET'])
def yearly_data_list():
    since = request.args.get('since', default = 2020, type = int)
    upto = request.args.get('upto', default = None)
    data = get_yearly_data_list(since,upto)

    JSONResponse = {
        "ok":True,
        "data":data,
        "message":"Sukses"
    }
    return jsonify(JSONResponse)

@app.route('/yearly/<year>', methods=['GET'])
def specific_year_data(year):
    data = get_specific_year_data(year)

    JSONResponse = {
        "ok":True,
        "data":data,
        "message":"Sukses"
    }
    return jsonify(JSONResponse)

@app.route('/monthly', methods=['GET'])
def monthly_data_list():
    since = request.args.get('since', default = '2020.03', type = str)
    upto = request.args.get('upto', default = None)
    data = get_monthly_data_list(since,upto)

    JSONResponse = {
        "ok":True,
        "data":data,
        "message":"Sukses"
    }
    return jsonify(JSONResponse)


@app.route('/monthly/<year>', methods=['GET'])
def monthly_data_by_year(year):
    
    since = request.args.get('since', default = '2020.03', type = str)
    upto = request.args.get('upto', default = None)
    data = get_monthly_data_by_year(int(year),since,upto)

    JSONResponse = {
        "ok":True,
        "data":data,
        "message":"Sukses"
    }
    return jsonify(JSONResponse)

@app.route('/monthly/<year>/<month>')
def specific_monthly_data(year,month):
    data = get_specific_month_data(year,month)

    JSONResponse = {
        "ok":True,
        "data":data,
        "message":"Sukses"
    }
    return jsonify(JSONResponse)

@app.route('/daily', methods=['GET'])
def daily_data_list():
    
    since = request.args.get('since', default = '2020.03.02', type = str)
    upto = request.args.get('upto', default = None)
    data = get_daily_data_list(since,upto)

    JSONResponse = {
        "ok":True,
        "data":data,
        "message":"Sukses"
    }
    return jsonify(JSONResponse)

@app.route('/daily/<year>', methods=['GET'])
def daily_data_by_year(year):
    
    since = request.args.get('since', default = '2020.03.02', type = str)
    upto = request.args.get('upto', default = None)
    data = get_daily_data_by_year(int(year),since,upto)

    JSONResponse = {
        "ok":True,
        "data":data,
        "message":"Sukses"
    }
    return jsonify(JSONResponse)

@app.route('/daily/<year>/<month>', methods=['GET'])
def daily_data_by_month(year,month):
    
    since = request.args.get('since', default = '2020.03.02', type = str)
    upto = request.args.get('upto', default = None)
    data = get_daily_data_by_month(year,month,since,upto)

    JSONResponse = {
        "ok":True,
        "data":data,
        "message":"Sukses"
    }
    return jsonify(JSONResponse)

@app.route('/daily/<year>/<month>/<day>', methods=['GET'])
def specific_daily_data(year,month,day):

    data = get_specific_daily_data(year,month,day)

    JSONResponse = {
        "ok":True,
        "data":data,
        "message":"Sukses"
    }
    return jsonify(JSONResponse)

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)