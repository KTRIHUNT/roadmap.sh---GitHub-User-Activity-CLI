second project goin into da portfolio. who hirin me

# GitHub User Activity CLI
### Solved for roadmap.sh

If you want to know the description of and requirements for this project, you may read it on https://roadmap.sh/projects/github-user-activity

#### Usage

Download the python file from the repository and open its directory in a CLI (Command Line Interface).
Run commands through python and main.py, Example: `>> python main.py --list todo`

#### Commands

| Command                                              | Usage                                                                               | Arguments                                                                                                |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| --add [DESCRIPTION]<br>-a [DESCRIPTION]              | Adds a task to the task tracker.<br>i.e. "--add Walk the dog"                        | DESCRIPTION: Description of your task.                                                                   |
| --delete [ID]<br>-d [ID]                             | Deletes a task in the task tracker.<br>i.e. "--delete 1".                            | ID: ID number associated with an existing task.                                                          |
| --update [ID] [DESCRIPTION]<br>-u [ID] [DESCRIPTION] | Updates a task's description in the task tracker.<br>i.e. "--update 1 Do the dishes" | ID: ID number associated with an existing task.<br>DESCRIPTION: Description of your task.                |
| --list [optional: STATUS]<br>-l [optional: STATUS]   | Lists all tasks in the task tracker, including task description, id, date created, last updated, and status.<br>i.e. "--list todo". | STATUS: Status of the task (Allowed: todo, done, wip) |
| --mark [ID] [STATUS]<br>-m [ID] [STATUS]             | Marks an existing task with a new status.<br>i.e. "--mark 1 todo".                   | ID: ID number associated with an existing task.<br>STATUS: Status of the task (Allowed: todo, done, wip) |
| --help<br>-h                                         | argparse built-in command, will display a less verbose version of this section.     |                                                                                                          |


#### Dependencies

- Python 3 from https://www.python.org/downloads/
- _requests_ Library (install through the terminal, i.e. C:\> python -m pip install requests)
