# Project Management CLI Tool

A command-line interface (CLI) tool for managing users, projects, and tasks. Designed for development teams to handle project organization through structured commands, with persistent storage and clean output.

## Setup Instructions:
1. Clone the Repository from GitHub
2. Install Pipenv via:
    pip3 install pipenv
3. Install Dependencies via:
    pipenv install
4. Activate the Virtual Environment via:
    pipenv shell

## Running CLI Commands
All commands are run through the main.py file using Python:
    python main.py <command> [options]

**Available Commands**
Users:
- Add a user via:
    python main.py add-user --name "Matt" --email "matt@gmail.com"
- List all users via:
    python main.py list-users

Projects:
- Add a project via:
    python main.py add-project --user "Matt" --title "Read a Book" --description "Finish Al Pacino's autobiography" --due 2025-09-30
- List all projects via:
    python main.py list-projects

Tasks:
- Add a task to a project via:
    python main.py add-task --project "Website Redesign" --title "Design mockups" --assigned "Matt" --status "incomplete"
- List all tasks via:
    python main.py list-tasks
- Mark a task as complete via:
    python main.py complete-task --id 1

## Features:
- Create and manage users, projects, and tasks.
- Assign projects to users and tasks to projects.
- Mark tasks as complete.
- Store data persistently using JSON files.
- View all data in well-formatted terminal tables using the rich library.

## Testing:
This project uses pytest for testing.
Run all tests via:
    pytest
Test coverage includes:
- Core data models (User, Project, Task)
- Basic CLI behavior (e.g. --help command)
All test files are located in the tests/ directory.
