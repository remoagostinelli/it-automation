#!/usr/bin/env python3

import sys
import subprocess



with open(sys.argv[1], 'r', encoding='UTF-8') as oldFiles:
        for file in oldFiles.readlines():
                file = file.strip()
                new_file_name = file.replace("jane", "jdoe")
                subprocess.run(["mv", file, new_file_name])