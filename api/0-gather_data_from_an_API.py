#!/usr/bin/python3
import requests
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("user", type=int, help="user id")

    args = parser.parse_args()

    user = requests.get("https://jsonplaceholder.typicode.com/users/" + f"{args.user}")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/" + f"{args.user}")
    
    total_tasks = 0
    completed_tasks = 0

    name = user.json().get("name")

    for task in todos.json():
        if task.get("userId") == args.user:
            total_tasks += 1
            if task.get("completed") == True:
                completed_tasks += 1

    print(f"Employee {name} is done with tasks({completed_tasks}/{total_tasks}):")


if __name__ == "__main__":
    main()
