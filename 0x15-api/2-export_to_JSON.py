#!/usr/bin/python3

"""

A script to export data in the CSV format.
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        user_id = str(argv[1])
        user_url = "https://jsonplaceholder.typicode.com/users/"+user_id
        user_data = requests.get(user_url).json()
        json_dict = {}

        # confirm if the user id is the one fetched
        user_ID = user_data.get("id")
        if int(user_id) == user_ID:
            employee_name = user_data.get("username")
            tasks_url = "https://jsonplaceholder.typicode.com/todos/"
            tasks = requests.get(tasks_url).json()
            output_data = []
            for i in range(len(tasks)):
                if user_ID == tasks[i].get("userId"):
                    my_dict = {}
                    my_dict['task'] = tasks[i].get("title")
                    my_dict['completed'] = tasks[i].get("completed")
                    my_dict['username'] = employee_name
                    output_data.append(my_dict)

            json_dict[user_ID] = output_data
        else:
            raise ValueError("Wrong user")
    else:
        raise ValueError("No arguments provided")

    # serializing json
    json_output = json.dumps(json_dict)

    # writing the data to JSON file
    with open("{}.json".format(user_ID), "w") as output_file:
        output_file.write(json_output)
