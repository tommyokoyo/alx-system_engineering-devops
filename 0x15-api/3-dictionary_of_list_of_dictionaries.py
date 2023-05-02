#!/usr/bin/python3

"""

A script to export data in the CSV format.
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    users_url = "https://jsonplaceholder.typicode.com/users"
    tasks_url = "https://jsonplaceholder.typicode.com/todos/"
    user_data = requests.get(users_url).json()
    tasks = requests.get(tasks_url).json()
    json_dict = {}

    for user in range(len(user_data)):
        user_id = user_data[user].get("id")
        output_data = []
        for i in range(len(tasks)):
            if user_id == tasks[i].get("userId"):
                my_dict = {}
                my_dict['task'] = tasks[i].get("title")
                my_dict['completed'] = tasks[i].get("completed")
                my_dict['username'] = user_data[user].get("username")
                output_data.append(my_dict)
                json_dict[user_id] = output_data

    # serializing json
    json_output = json.dumps(json_dict)

    # writing the data to JSON file
    with open("todo_all_employees.json", "w") as output_file:
        output_file.write(json_output)
