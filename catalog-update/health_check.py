#!/usr/bin/env python3

import shutil
import psutil
import socket
from emails import generate_error_report, send_email


def main():
    disk = "/"
    time = 1
    du = check_disk_usage(disk)
    cu = check_cpu_usage(time)
    mem = check_ram_usage()
    is_localhost = check_localhost()
    print(du, cu, mem, is_localhost)
    if du and cu and mem and is_localhost:
        print("Everything is OK!")
    else:
        if not cu:
            title = "Error - CPU usage is over 80%"
        elif not du:
            title = "Error - Available disk space is less than 20%"
        elif not mem:
            title = "Error - Available memory is less than 500MB"
        else:
            title = "Error - localhost cannot be resolved to 127.0.0.1"
        print(title)
        sender = "automation@example.com"
        recipient = "student-02-96927976bbbc@example.com"
        body = "Please check your system and resolve the issue as soon as possible."
        message = generate_error_report(sender, recipient, title, body)
        send_email(message)
        print("An email has been sent")


def check_disk_usage(disk):
    """Returns False if free disk space is less than 20%."""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free >= 20


def check_cpu_usage(time):
    """Returns False if CPU usage is over 80%."""
    cu = psutil.cpu_percent(time)
    return cu <= 80


def check_ram_usage():
    """Returns False if RAM available is less than 500 MB."""
    threshold = 500 * 1024 * 1024 # 500 MB
    mem = psutil.virtual_memory()
    return mem.available >= threshold


def check_localhost():
    """Returns False if localhost cannot be resolved to 127.0.0.1"""
    localhost = socket.gethostbyname("localhost")
    if localhost == "127.0.0.1":
        return True
    return False


if __name__ == "__main__":
    main()