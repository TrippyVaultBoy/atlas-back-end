#!/usr/bin/python3
"""Includes employee_todo_list"""
import requests
import sys


def employee_todo_list(employee_id):
    """For a given employee ID, returns information
    about his/her TODO list progress."""
    api_url = 'https://jsonplaceholder.typicode.com'

    response = requests.get(f'{api_url}/users/{employee_id}')
    user_data = response.json()

    if response.status_code != 200 or not user_data:
        print(f"Error: Employee with ID {employee_id} not found.")
        return

    employee_name = user_data['name']

    todos_response = requests.get(f'{api_url}/users/{employee_id}/todos')
    todo_data = todos_response.json()

    if response.status_code != 200 or not todo_data:
        print(f"Error: No tasks found for employee {employee_id}.")
        return

    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task.get('completed')]
    finished_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          finished_tasks,
                                                          total_tasks))

    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    employee_todo_list(employee_id=sys.argv[1])
