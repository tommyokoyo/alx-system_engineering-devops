#!/usr/bin/python3

"""

A script to export data in the CSV format.
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        user_id = str(argv[1])
        user_url = "https://jsonplaceholder.typicode.com/users/"+user_id
        user_data = requests.get(user_url).json()

        # confirm if the user id is the one fetched
        user_ID = user_data.get("id")
        if int(user_id) == user_ID:
            employee_name = user_data.get("name")
            tasks_url = "https://jsonplaceholder.typicode.com/todos/"
            tasks = requests.get(tasks_url).json()
            task_completed = 0
            total_tasks = 0
            tasks_title = []
            task_status = []

            for i in tasks:
                if user_ID == i.get("userId"):
                    status = i.get("completed")
                    task_status.append(status)
                    if status is True:
                        task_completed += 1
                        total_tasks += 1
                        tasks_title.append(i.get("title"))
                    else:
                        total_tasks += 1
                else:
                    pass
            print("Employee {0} is done with tasks({1}/{2}):".format(
                employee_name, task_completed, total_tasks))

            for j in tasks_title:
                print("\t {}".format(j))
        else:
            raise ValueError("Wrong user")
    else:
        raise ValueError("No arguments provided")

"""

Exports the data to a csv file
"""
# writing the data to csv file
with open("{}.csv".format(user_id), mode="w") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for i in range(len(tasks_title)):
        writer.writerow([user_ID, employee_name,
                         task_status[i], tasks_title[i]])
