import requests
import argparse
import datetime


# Total: 4
# Employees:
# - Apr 1, John Doe
# - Apr 10, Patrick Brown
# ....
def print_response(resp:dict):
    print(f'Total: {resp['total']}\nEmployees:')
    for i in resp['employees']:
        date = datetime.datetime.strptime(i['birthday'], '%Y-%m-%d')
        print(f'- {date.strftime("%b %d")}, {i['name']}')


url = 'http://127.0.0.1:5000/{endpoint}'
headers = {'Content-Type': 'application/json'}

parser = argparse.ArgumentParser()
parser.add_argument('params', nargs='+')
args = parser.parse_args()

response = requests.get(url.format(endpoint=f'birthdays?month={args.params[0]}&department={args.params[1]}'), headers=headers)

if response.status_code == 200:
    print('Report for Engineering department for April fetched.')
    print_response(response.json())
else:
    print(f'GET request failed.\nCode: {response.status_code}.\nMessage: {response.text}')

# python fetch_report.py april Engineering