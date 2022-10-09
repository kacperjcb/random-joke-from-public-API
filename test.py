import requests
import json
import pprint
import yaml

companyName = input("Please input a company name. ")
dateFrom=input("Please input start date ")
url = "https://api.stockdata.org/v1/data/eod?symbols="+companyName+"&date_from="+dateFrom+"&api_token=d4BNfm1S9fHBIgiXf4WF1EHzB6HFTsInADvEr7rW"
response = requests.get(url)
data = json.loads(response.text)
pprint.pprint(data['data'])
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump((data['data']), f, ensure_ascii=False, indent=4)
with open('data.json', 'r') as file:
    configuration = json.load(file)
with open('data.yaml', 'w') as yaml_file:
    yaml.dump(configuration, yaml_file)
with open('data.yaml', 'r') as yaml_file:
    print(yaml_file.read())



