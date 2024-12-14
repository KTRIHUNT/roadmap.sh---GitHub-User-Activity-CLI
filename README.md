second project goin into da portfolio. who hirin me

# GitHub User Activity CLI
### Solved for roadmap.sh

If you want to know the description of and requirements for this project, you may read it on https://roadmap.sh/projects/github-user-activity

#### Usage

Download the python file from the repository and open its directory in a CLI (Command Line Interface).<br>
Install pip dependencies. i.e. `>> python -m pip install -r requirements.txt`<br>
Run commands through python and main.py, a username or organization name is REQUIRED. Example: `>> python main.py KTRIHUNT`<br>
All other commands below are optional.

#### Commands

| Command                    | Usage                                                                                | Arguments                                         |
|----------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------|
| --verbose<br>-v            | Activity messages are now verbose, each type of event getting specified information. |                                                   |
| --external<br>-e           | Practically for searching organization activity.                                     |                                                   |
| --date<br>-d               | Appends the date of the event at the end of each activity message.                   |                                                   |
| --page [PAGE]<br>-p [PAGE] | Prints the next page of activity from the user/organization (~30 events per page).   | PAGE: Any valid page number (integer by default). |
| --help<br>-h               | argparse built-in command, will display a less verbose version of this section.      |                                                   |


#### Dependencies

- Python 3 from https://www.python.org/downloads/
- The following libraries are installed with `>>pip install -r requirements.txt`"
  - requests 
