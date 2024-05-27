# Task Manager CLI

A simple Command-Line Interface (CLI) tool for managing tasks.

## Features

- Add a new task
- List all tasks
- Mark a task as completed
- Remove a task
- Save tasks to a file

## Installation

```bash
pip install -r requirements.txt
python setup.py install
# Add a new task
task-manager add "New task description"

# List all tasks
task-manager list

# Mark a task as completed
task-manager complete 1

# Remove a task
task-manager remove 1
