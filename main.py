import requests
import json
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('username')

args = parser.parse_args()


api = requests.get(f'https://api.github.com/users/{args.username}/events')

if api.status_code == 404:
    print("Invalid User!")
else:
    file = open('user.json', 'w')
    file.write(api.text)
    file.close()