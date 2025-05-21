#!/usr/bin/python3

import json
import os
import sys
import argparse
from datetime import datetime

def get_next_id(path):
    try:
        with open(path, 'r', encoding='utf-8') as database:
            tasks = json.load(database)
        if not tasks:
            return 1
        else:
            return max(task['id'] for task in tasks) + 1
    except FileNotFoundError:
        return 1 

def add_task(task):
    with open('database.json', 'w', encoding='utf-8') as database:
        data = [
            {
                "id":f'{get_next_id("database.json")}',
                "description":f'{task}',
                "status":"todo",
                "createdAt":f'{datetime.now()}',
                "updatedAt":"",

            }
        ]
        json.dump(data, database)
    print("Task added succesfully")

def main():
    task = sys.argv[1]
    if task:
        add_task(task)

if __name__ == '__main__':
    main()