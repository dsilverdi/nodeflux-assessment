from datetime import date, datetime
from dateutil.parser import parse
import requests

baseUrl = 'https://data.covid19.go.id/public/api/update.json'

def get_updated_data():
    r = requests.get(baseUrl)
    r = r.json()

    updatePenambahan = r["update"]["penambahan"]
    total = r["update"]["total"]

    payload = {
        "total_positive": total["jumlah_positif"],
        "total_recoverd":total["jumlah_sembuh"],
        "total_deaths":total["jumlah_meninggal"],
        "total_active":total["jumlah_dirawat"],
        "new_positive":updatePenambahan["jumlah_positif"],
        "new_recovered":updatePenambahan["jumlah_sembuh"],
        "new_deaths":updatePenambahan["jumlah_meninggal"],
        "new_active":updatePenambahan["jumlah_dirawat"],
    }

    return payload

def get_specific_year_data(year):
    r = requests.get(baseUrl)
    r = r.json()

    year = int(year)
    payload = {
        "year":year,
        "positive":0,
        "active":0,
        "deaths":0,
        "recovered":0
    }

    dataharian = r["update"]["harian"]
    
    for data in dataharian:
        yeardata = parse(str(data["key_as_string"])).year
      
        if year == yeardata:
            payload["positive"] += data["jumlah_positif"]["value"]
            payload["active"] += data["jumlah_dirawat"]["value"]
            payload["deaths"] += data["jumlah_meninggal"]["value"]
            payload["recovered"] += data["jumlah_sembuh"]["value"]
        

    return payload

def get_yearly_data_list(sinceYear, uptoYear=None):
    r = requests.get(baseUrl)
    r = r.json()

    dataharian = r["update"]["harian"]
    payloadList = []

    if uptoYear == None:
        uptoYear = datetime.today().year

    i = 0
    while i < len(dataharian):
        data = dataharian[i] 
        year = parse(str(data["key_as_string"])).year
        
        if sinceYear <= year and uptoYear >= year:
            # print(year)            
            payload = {
                "year":year,
                "positive":0,
                "active":0,
                "deaths":0,
                "recovered":0
            }

            currentYear = year
            while currentYear == year and i < len(dataharian):
                payload["positive"] += data["jumlah_positif"]["value"]
                payload["active"] += data["jumlah_dirawat"]["value"]
                payload["deaths"] += data["jumlah_meninggal"]["value"]
                payload["recovered"] += data["jumlah_sembuh"]["value"]
                
                i += 1
                if i < len(dataharian):
                    data = dataharian[i]
                    currentYear = parse(str(data["key_as_string"])).year
                
            payloadList += [payload]
        else:
            i+=1

    return payloadList


def get_monthly_data_list(since, upto=None):
    r = requests.get(baseUrl)
    r = r.json()
    

    payloadList = []
    dataharian = r["update"]["harian"]
    
    if upto == None:
        upto = datetime.today().date()
    else:
        upto = datetime.strptime(upto,'%Y.%m').date()

    since = datetime.strptime(since,'%Y.%m').date()

    i = 0
    while i < len(dataharian):
        data = dataharian[i]
        date = parse(str(data["key_as_string"]))
        
        if (date.date() >= since and date.date() <= upto):
            payload = {
                "month":datetime.strftime(date,'%Y-%m'),
                "positive":0,
                "active":0,
                "deaths":0,
                "recovered":0
            }
            currentMonth = date.month
            while currentMonth == date.month and i < len(dataharian):
                payload["positive"] += data["jumlah_positif"]["value"]
                payload["active"] += data["jumlah_dirawat"]["value"]
                payload["deaths"] += data["jumlah_meninggal"]["value"]
                payload["recovered"] += data["jumlah_sembuh"]["value"]
                
                i += 1
                if i < len(dataharian):
                    data = dataharian[i]
                    currentMonth = parse(str(data["key_as_string"])).month
            
            payloadList += [payload]
        else:
            i+=1    
            
    return payloadList

def get_monthly_data_by_year(year, since, upto=None):
    r = requests.get(baseUrl)
    r = r.json()
    

    payloadList = []
    dataharian = r["update"]["harian"]

    if upto == None:
        upto = datetime.today().date()
    else:
        upto = datetime.strptime(upto,'%Y.%m').date()

    since = datetime.strptime(since,'%Y.%m').date()
    
    i = 0
    while i < len(dataharian):
        data = dataharian[i]
        date = parse(str(data["key_as_string"]))
        
        if (date.year == year and since <= date.date() and upto >= date.date()):
            payload = {
                "month":datetime.strftime(date,'%Y-%m'),
                "positive":0,
                "active":0,
                "deaths":0,
                "recovered":0
            }
            currentMonth = date.month
            while currentMonth == date.month and i < len(dataharian):
                payload["positive"] += data["jumlah_positif"]["value"]
                payload["active"] += data["jumlah_dirawat"]["value"]
                payload["deaths"] += data["jumlah_meninggal"]["value"]
                payload["recovered"] += data["jumlah_sembuh"]["value"]
                
                i += 1
                if i < len(dataharian):
                    data = dataharian[i]
                    currentMonth = parse(str(data["key_as_string"])).month
            
            payloadList += [payload]
        else:
            i+=1    
            
    return payloadList

def get_specific_month_data(year,month):
    r = requests.get(baseUrl)
    r = r.json()

    payload = {
        "month":"{}-{}".format(year,month),
        "positive":0,
        "active":0,
        "deaths":0,
        "recovered":0
    }

    dataharian = r["update"]["harian"]
    
    for data in dataharian:
        date = parse(str(data["key_as_string"]))
      
        if int(year) == date.year and int(month) == date.month:
            payload["positive"] += data["jumlah_positif"]["value"]
            payload["active"] += data["jumlah_dirawat"]["value"]
            payload["deaths"] += data["jumlah_meninggal"]["value"]
            payload["recovered"] += data["jumlah_sembuh"]["value"]
        

    return payload

def get_daily_data_list(since, upto=None):
    r = requests.get(baseUrl)
    r = r.json()

    payloadList = []    
    payload = {}

    if upto == None:
        upto = datetime.today().date()
    else:
        upto = datetime.strptime(upto,'%Y.%m.%d').date()

    since = datetime.strptime(since,'%Y.%m.%d').date()

    dataharian = r["update"]["harian"]

    print(upto, since)
    for data in dataharian:
        payload = {
            "date":"",
            "positive":0,
            "active":0,
            "deaths":0,
            "recovered":0,
        }
        date = parse(str(data["key_as_string"])).date()
        if since <= date and upto >= date:
            print(date)
            payload["date"] = str(date)
            payload["positive"] = data["jumlah_positif"]["value"]
            payload["active"] = data["jumlah_dirawat"]["value"]
            payload["deaths"] = data["jumlah_meninggal"]["value"]
            payload["recovered"] = data["jumlah_sembuh"]["value"]
            payloadList += [payload]

    return payloadList

def get_daily_data_by_year(year, since, upto=None):
    r = requests.get(baseUrl)
    r = r.json()

    payloadList = []    
    payload = {}

    dataharian = r["update"]["harian"]

    if upto == None:
        upto = datetime.today().date()
    else:
        upto = datetime.strptime(upto,'%Y.%m.%d').date()

    since = datetime.strptime(since,'%Y.%m.%d').date()

    for data in dataharian:
        payload = {
            "date":"",
            "positive":0,
            "active":0,
            "deaths":0,
            "recovered":0,
        }
        date = parse(str(data["key_as_string"]))
        if year == date.year and since <= date.date() and upto >= date.date():
            payload["date"] = str(date.date())
            payload["positive"] = data["jumlah_positif"]["value"]
            payload["active"] = data["jumlah_dirawat"]["value"]
            payload["deaths"] = data["jumlah_meninggal"]["value"]
            payload["recovered"] = data["jumlah_sembuh"]["value"]
            payloadList += [payload]

    return payloadList

def get_daily_data_by_month(year, month, since, upto):
    r = requests.get(baseUrl)
    r = r.json()

    payloadList = []    
    payload = {}

    dataharian = r["update"]["harian"]

    if upto == None:
        upto = datetime.today().date()
    else:
        upto = datetime.strptime(upto,'%Y.%m.%d').date()

    since = datetime.strptime(since,'%Y.%m.%d').date()

    for data in dataharian:
        payload = {
            "date":"",
            "positive":0,
            "active":0,
            "deaths":0,
            "recovered":0,
        }
        date = parse(str(data["key_as_string"]))
        if int(year) == date.year and int(month) == date.month and since <= date.date() and upto >= date.date():
            payload["date"] = str(date.date())
            payload["positive"] = data["jumlah_positif"]["value"]
            payload["active"] = data["jumlah_dirawat"]["value"]
            payload["deaths"] = data["jumlah_meninggal"]["value"]
            payload["recovered"] = data["jumlah_sembuh"]["value"]
            payloadList += [payload]

    return payloadList

def get_specific_daily_data(year, month, day):
    r = requests.get(baseUrl)
    r = r.json()
   
    payload = {}

    dataharian = r["update"]["harian"]

    for data in dataharian:
        date = parse(str(data["key_as_string"]))
        if int(year) == date.year and int(month) == date.month and int(day) == date.day:
            payload["date"] = str(date.date())
            payload["positive"] = data["jumlah_positif"]["value"]
            payload["active"] = data["jumlah_dirawat"]["value"]
            payload["deaths"] = data["jumlah_meninggal"]["value"]
            payload["recovered"] = data["jumlah_sembuh"]["value"]

    return payload


# print(get_monthly_data_list('2020.02','2020.05'))
# print(get_monthly_data_by_year(2020))
# print(get_specific_month_data(2020,'03'))

# print(get_specific_year_data(2020))
# print(get_yearly_data_list(2020))

# print(get_daily_data_list('2020.04.01','2020.04.03'))
# print(get_daily_data_list('2020.03.02'))
# print(get_daily_data_list('2020.03.02'))