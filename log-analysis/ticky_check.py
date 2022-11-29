#!/usr/bin/env python3

import re
import operator
import random
import csv

errors_logs = {}
usersMessages = {}
error_count = 0
info_count = 0
log_type_regex = r"ticky: (ERROR|INFO): ([\w ].*) "
info_regex = r"ticky: INFO: ([\w ].*) "
user_regex = r"\((\w+)\)|\((\w+\.\w+)\)"
log = open("syslog.log")

users = set()
for line in log:
    user = re.search(user_regex, line)
    users.add(user[0].strip("()"))

def findTheUser(users):
    for i in users:
        if i in line:
            usersMessages[i] = [str(info_count), str(error_count)]

fetches = []
for line in log:
    match = re.search(log_type_regex, line)
    fetch = match[0].strip()
    fetches.append(fetch)
    if "ERROR" in line:
        if fetch not in errors_logs:
            errors_logs[fetch] = 1
            error_count = 1
            findTheUser(users)
        else:
            errors_logs[fetch] += 1
            error_count = errors_logs[fetch]
            findTheUser(users)
    elif "INFO" in line:
        if fetch not in usersMessages:
            usersMessages[fetch] = 1
            info_count = 1
            findTheUser(users)
        else:
            usersMessages[fetch] += 1
            info_count = usersMessages[fetch]
            findTheUser(users)

log.close()

users_logs = dict(usersMessages)
for key in usersMessages:
    if key in fetches:
        del users_logs[key]

sorted_errors_logs = dict(sorted(errors_logs.items(), key=operator.itemgetter(1), reverse=True))
sorted_users_logs = dict(sorted(users_logs.items(), key=operator.itemgetter(0)))

with open('error_message.csv', 'w', encoding='UTF-8') as csv_error:
    writer = csv.writer(csv_error)
    writer.writerow(['Error', 'Count'])
    for element in sorted_errors_logs:
        writer.writerow(element)

with open('user_statistics.csv', 'w', encoding='UTF-8') as csv_stats:
    fieldnames = ['Username', 'INFO', 'ERROR']
    writer = csv.DictWriter(csv_stats, fieldnames=fieldnames)
    writer.writeheader()
    for key, value in sorted_users_logs.items():
        writer.writerow({'Username': key, 'INFO': value[0], 'ERROR': value[1]})