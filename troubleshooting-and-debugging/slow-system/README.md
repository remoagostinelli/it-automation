# Fix a Slow System with Python
A media production company uses Network-Attached Storage (NAS) to store all data generated daily (e.g., videos, photos). One of the daily tasks is to back up the data in the production NAS (mounted at /data/prod on the server) to the backup NAS (mounted at /data/prod_backup on the server). A former member of the team developed a Python script (full path /scripts/dailysync.py) that backs up data daily. But recently, there's been a lot of data generated and the script isn't catching up to the speed. As a result, the backup process now takes more than 20 hours to finish, which isn't efficient at all for a daily backup.

- Identify what limits the system performance: I/O, Network, CPU, or Memory
- Use rsync command instead of cp to transfer data
- Get system standard output and manipulate the output
- Find differences between threading and multiprocessing