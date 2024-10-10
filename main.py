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
parser.add_argument('-p', '--page', type=int)

args = parser.parse_args()
print("Searching for user...")

response = requests.get(f'https://api.github.com/users/{args.username}/events?page={args.page}')
orgs_response = requests.get(f'https://api.github.com/orgs/{args.username}')

if response.status_code == 404:
    print("Invalid User!")
elif response.status_code != 200:
    print(f"Error! Github returned status code {response.status_code}: {response.reason}")
    print(f"Error message: {response.json()['message']}")
else:
    if orgs_response.status_code == 200:
        if not args.external:
            print(f"Warning: {args.username} is an organization! use --external to show activity associated with the organization.")
        else:
            print("Organization Found! Displaying recent activity...")
    else:
        print("User Found! Displaying recent activity...")
    time.sleep(2)

    file = response.json()
    for event in file:
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
                case 'ReleaseEvent':
                    print(f"{event['payload']['action'].capitalize()} release \'{event['payload']['release']['name']}\' in {event['repo']['name']}", end=print_end)
                case 'GollumEvent':
                    print(', '.join(f"{page['action'].capitalize()} wiki page \'{page['title']}\'" for page in event['payload']['pages']), end=' ')
                    print(f"for repository {event['repo']['name']}", end=print_end)
                case 'MemberEvent':
                    print(f"{event['payload']['action'].capitalize()} collaborator \'{event['payload']['member']['login']}\' in {event['repo']['name']}", end=print_end)
                case _:
                    print(f"{event['type']} in {event['repo']['name']}", end=print_end)
        else:
            print(f"{event['type']} in {event['repo']['name']}", end=print_end)