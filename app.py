import requests
import json
import datetime
import yaml
from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
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
    cursor = mysql.connection.cursor()
    query = '''INSERT INTO `chuck`(`value`,`dataTime`) VALUES (%s,%s)'''
    tuple1 = (d, date_time)
    cursor.execute(query, tuple1)
    mysql.connection.commit()
    cursor.close()
    return render_template("index.html", content=d)


@app.route('/all/', methods=['GET'])
def index2():
    cursor = mysql.connection.cursor()
    query = '''SELECT distinct value from chuck '''
    cursor.execute(query)
    list_1 = list()

    for row in cursor:
        list_1.append(row)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(list_1, f, ensure_ascii=False, indent=4)
        with open('data.json', 'r') as file:
            configuration = json.load(file)
        with open('data.yaml', 'w') as yaml_file:
            yaml.dump(configuration, yaml_file)
    return render_template("index2.html", list_1=list_1)


app.run(debug=True)
app.run(host='127.0.0.1', port=5000)
