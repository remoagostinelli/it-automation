#!/usr/bin/env python3

import os
from datetime import date
import reports, emails


def main():
  home = os.path.expanduser("~")
  path = f"{home}/supplier-data/descriptions"
  files = os.listdir(path)
  paragraphs = ""

  for file in files:

    with open(f"{path}/{file}", "r") as f:
      lines = f.read().splitlines()
      while lines[-1].strip() == "":
        del lines[-1]
      del lines[-1]
      lines[0] = "name: " + lines[0]
      lines[1] = "weight: " + lines[1]
      print(lines)
      paragraph = "<br/>".join(lines) + "<br/><br/>"
      paragraphs += paragraph

  today = date.today()

  reports.generate_report("/tmp/processed.pdf", f"Processed Update on {today.strftime('%B %d, %Y')}", paragraphs)

  message = emails.generate_email("automation@example.com", "student-02-96927976bbbc@example.com", "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "/tmp/processed.pdf")

  emails.send_email(message)


if __name__ == "__main__":
  main()
