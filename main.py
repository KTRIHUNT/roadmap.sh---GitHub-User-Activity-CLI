import requests
import json
from argparse import ArgumentParser
import time
import os

parser = ArgumentParser()
parser.add_argument('username')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-e', '--external', action='store_true')
parser.add_argument('-d', '--date', action='store_true')

args = parser.parse_args()
print("Searching for user...")

api = requests.get(f'https://api.github.com/users/{args.username}/events')

if api.status_code == 404:
    print("Invalid User!")
elif api.status_code != 200:
    print(f"Error! Github returned status code {api.status_code}")
else:
    print("User Found! Displaying recent activity...")
    time.sleep(1)

    file = open('user.json', 'w',encoding='utf-8')
    file.write(api.text)
    file.close()

    with open('user.json',encoding='utf-8') as file:
        file_list = json.load(file)
        for event in file_list:
            if args.date:
                event_date, event_time = event['created_at'][:-1].split('T')
                print_end = f" at {event_time} UTC, {event_date}\n"
            else:
                print_end = '\n'

            if event['actor']['login'] != args.username:
                if not args.external:
                    continue
                else:
                    print(event['actor']['display_login'], end=' ')

            if args.verbose:
                match event['type']:
                    case 'PushEvent':
                        print(f"Pushed {event['payload']['size']} commit(s) to {event['repo']['name']}", end=print_end)
                    case 'CreateEvent':
                        if event['payload']['ref_type'] == 'repository':
                            print(f"Created repository {event['repo']['name']}", end=print_end)
                        else:
                            print(f"Created {event['payload']['ref_type']} \'{event['payload']['ref']}\' in {event['repo']['name']}", end=print_end)
                    case 'PullRequestEvent':
                        action = ' '.join(i.capitalize() for i in event['payload']['action'].split('_'))
                        print(f"{action} pull request \'{event['payload']['pull_request']['title']}\' in {event['repo']['name']}", end=print_end)
                    case 'DeleteEvent':
                        print(f"Deleted {event['payload']['ref_type']} \'{event['payload']['ref']}\' in {event['repo']['name']}", end=print_end)
                    case 'IssuesEvent':
                        print(f"{event['payload']['action'].capitalize()} issue \'{event['payload']['issue']['title']}\' in {event['repo']['name']}", end=print_end)
                    case 'PublicEvent':
                        print(f"Made repository {event['repo']['name']} public! Yay!", end=print_end)
                    case 'WatchEvent':
                        print(f"Starred {event['repo']['name']}", end=print_end)
                    case 'PullRequestReviewEvent':
                        print(f"Accepted review for pull request \'{event['payload']['pull_request']['title']}\' in {event['repo']['name']}", end=print_end)
                    case 'PullRequestReviewCommentEvent':
                        print(f"Commented on pull request \'{event['payload']['pull_request']['title']}\' in {event['repo']['name']}", end=print_end)
                    case 'IssueCommentEvent':
                        print(f"Commented on issue \'{event['payload']['issue']['title']}\' in {event['repo']['name']}", end=print_end)
                    case _:
                        print(f"{event['type']} in {event['repo']['name']}", end=print_end)
            else:
                print(f"{event['type']} in {event['repo']['name']}", end=print_end)

if os.path.exists("user.json"):
    os.remove("user.json")