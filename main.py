# main.py

import argparse

from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import load_data, save_data
from rich.console import Console
from rich.table import Table

console = Console()

USERS_FILE = "data/users.json"
PROJECTS_FILE = "data/projects.json"
TASKS_FILE = "data/tasks.json"

def add_user(name, email):
    users_data = load_data(USERS_FILE)  # Loads existing users
    new_user = User(name, email)    # Creates new user
    users_data.append(new_user.to_dict())   # Adds new user to data list
    save_data(USERS_FILE, users_data)   # Saves updated list of users
    console.print(f"[green]User added:[/] {new_user}")

def list_users():
    users_data = load_data(USERS_FILE)
    if not users_data:
        console.print("[bold red]No users found.[/]")
        return
    
    table = Table(title="Users")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Email", style="magenta")

    for data in users_data:
        user = User.from_dict(data)
        table.add_row(str(user.id), user.name, user.email)

    console.print(table)

def add_project(user_name, title, description, due_date):
    users_data = load_data(USERS_FILE)

    # Validation for existing user
    if not any(user["name"].strip().lower() == user_name.strip().lower() for user in users_data):   # Upper and lowercase spellings are equal
        console.print(f"[bold red]Error:[/] User '{user_name}' does not exist.")
        return

    projects_data = load_data(PROJECTS_FILE)
    new_project = Project(title, description, due_date, user_name)
    projects_data.append(new_project.to_dict())
    save_data(PROJECTS_FILE, projects_data)

    console.print(f"[green]Project added:[/] {new_project}")

def list_projects():
    projects_data = load_data(PROJECTS_FILE)
    if not projects_data:
        console.print("[bold red]No projects found.[/]")
        return

    table = Table(title="Projects")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="green")
    table.add_column("Due Date", style="yellow")
    table.add_column("Owner", style="magenta")

    for data in projects_data:
        project = Project.from_dict(data)
        table.add_row(str(project.id), project.title, project.due_date, project.user_name)

    console.print(table)

def add_task(project_title, title, assigned_to, status):
    users_data = load_data(USERS_FILE)
    projects_data = load_data(PROJECTS_FILE)

    # Validation for assigned users
    if not any(user["name"] == assigned_to for user in users_data):
        console.print(f"[bold red]Error:[/] User '{assigned_to}' does not exist.")
        return
    # Validation for project titles
    if not any(project["title"] == project_title for project in projects_data):
        console.print(f"[bold red]Error:[/] Project '{project_title}' does not exist.")
        return

    tasks_data = load_data(TASKS_FILE)
    new_task = Task(title, status, assigned_to, project_title)
    tasks_data.append(new_task.to_dict())
    save_data(TASKS_FILE, tasks_data)

    console.print(f"[green]Task added:[/] {new_task}")

def list_tasks():
    tasks_data = load_data(TASKS_FILE)
    if not tasks_data:
        console.print("[bold red]No tasks found.[/]")
        return
    
    table = Table(title="Tasks")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="green")
    table.add_column("Status", style="yellow")
    table.add_column("Assigned To", style="magenta")
    table.add_column("Project", style="blue")

    for data in tasks_data:
        task = Task.from_dict(data)
        table.add_row(str(task.id), task.title, task.status, task.assigned_to, task.project_title)

    console.print(table)

def complete_task(task_id):
    tasks_data = load_data(TASKS_FILE)
    updated = False

    for task_dict in tasks_data:
        if task_dict["id"] == task_id:
            task_dict["status"] = "complete"
            updated = True
            print(f"Task marked as complete: [{task_dict['id']}] {task_dict['title']}")
            break

    if not updated:
        print(f"No task found with ID {task_id}")
        return
    
    save_data(TASKS_FILE, tasks_data)

def update_id_counters():
    users_data = load_data(USERS_FILE)
    projects_data = load_data(PROJECTS_FILE)
    tasks_data = load_data(TASKS_FILE)

    if users_data:
        User._id_counter = max(user["id"] for user in users_data) + 1
    else:
        User._id_counter = 1

    if projects_data:
        Project._id_counter = max(project["id"] for project in projects_data) + 1
    else:
        Project._id_counter = 1

    if tasks_data:
        Task._id_counter = max(task["id"] for task in tasks_data) + 1
    else:
        Task._id_counter = 1

if __name__ == "__main__":
    update_id_counters()

    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # add-user command
    add_user_parser = subparsers.add_parser("add-user", help="Add a new user")
    add_user_parser.add_argument("--name", required=True, help="Name of the user")
    add_user_parser.add_argument("--email", required=True, help="Email of the user")

    # list-users command
    list_users_parser = subparsers.add_parser("list-users", help="List all users")

    # add-project command
    add_project_parser = subparsers.add_parser("add-project", help="Add a new project")
    add_project_parser.add_argument("--user", required=True, help="Name of user for project")
    add_project_parser.add_argument("--title", required=True, help="Project title")
    add_project_parser.add_argument("--description", required=True, help="Project description")
    add_project_parser.add_argument("--due", required=True, help="Due date (YYYY-MM-DD)")

    # list-projects command
    list_projects_parser = subparsers.add_parser("list-projects", help="List all projects")

    # add-task command
    add_task_parser = subparsers.add_parser("add-task", help="Add a new task to a project")
    add_task_parser.add_argument("--project", required=True, help="Project title associated with task")
    add_task_parser.add_argument("--title", required=True, help="Title of the task")
    add_task_parser.add_argument("--assigned", required=True, help="User assigned to the task")
    add_task_parser.add_argument("--status", choices=["incomplete", "complete"], default="incomplete", help="Status of the task (default: incomplete)")

    # list-tasks command
    list_tasks_parser = subparsers.add_parser("list-tasks", help="List all tasks")

    # complete-task command
    complete_task_parser = subparsers.add_parser("complete-task", help="Mark a task as complete")
    complete_task_parser.add_argument("--id", type=int, required=True, help="ID of the task to mark complete")

    # Parse and route commands
    args = parser.parse_args()

    if args.command == "add-user":
        add_user(args.name, args.email)
    elif args.command == "list-users":
        list_users()
    elif args.command == "add-project":
        add_project(args.user, args.title, args.description, args.due)
    elif args.command == "list-projects":
        list_projects()
    elif args.command == "add-task":
        add_task(args.project, args.title, args.assigned, args.status)
    elif args.command == "list-tasks":
        list_tasks()
    elif args.command == "complete-task":
        complete_task(args.id)
    else:
        parser.print_help()
