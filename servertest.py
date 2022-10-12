import requests
import json
import datetime
from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


@app.route('/')
def index():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = json.loads(response.text)
    d = data["value"]
    now = datetime.datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    # t=now.strftime("%m/%d/%Y, %H:%M:%S")
    cursor = mysql.connection.cursor()
    query = '''INSERT INTO `chuck`(`id`,`value`,`dataTime`) VALUES (%s,%s,%s)'''
    tuple1 = ('', d, date_time)
    cursor.execute(query, tuple1)
    mysql.connection.commit()
    cursor.close()
    return render_template("index.html", content=d)


@app.route('/all/', methods=['GET'])
def index2():

        cursor = mysql.connection.cursor()
        query = '''SELECT value from chuck '''
        cursor.execute(query)
        list_1 = list()

        for row in cursor:
            list_1.append(row)
        print("dupa")
        print(len(list_1))
        return render_template("index2.html", list_1=list_1)


# @app.route('/<name>', methods=['GET', 'POST'])
# def page(name):
#     comName = name
#     url = "https://api.stockdata.org/v1/data/eod?symbols=" + comName + "&api_token=d4BNfm1S9fHBIgiXf4WF1EHzB6HFTsInADvEr7rW"
#     response = requests.get(url)
#     data = json.loads(response.text)
#     d = (data['data'])
#     pprint.pprint(data['data'])
#     r=requests.post(url, data=json.dumps(data['data']))
#     with open('data.json', 'w', encoding='utf-8') as f:
#         json.dump(requests.post(url, data=data), f, ensure_ascii=False, indent=4)
#     return d

app.run(debug=True)
app.run(host='127.0.0.1', port=5000)
