import requests
import json
from argparse import ArgumentParser
import time
import os

parser = ArgumentParser()
parser.add_argument('username')

args = parser.parse_args()
print("Searching for user...")

api = requests.get(f'https://api.github.com/users/{args.username}/events')

if api.status_code == 404:
    print("Invalid User!")
else:
    print("User Found! Displaying recent activity...")
    time.sleep(1)

    file = open('user.json', 'w')
    file.write(api.text)
    file.close()

    with open('user.json') as file:
        file_list = json.load(file)
        events = {}
        for event in file_list:
            try:
                events[event['type']] += 1
            except KeyError:
                events[event['type']] = 1
        print(events)
    
if os.path.exists("user.json"):
    os.remove("user.json")