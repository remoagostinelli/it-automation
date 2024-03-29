#!/usr/bin/env python3

import json
import locale
import sys
import reports, emails


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0}
  years = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item["total_sales"] > max_sales["total_sales"]:
      max_sales = item

    # TODO: also handle most popular car_year
    year = item["car"]["car_year"]
    if year not in years:
      years[year] = item["total_sales"]
    else:
      years[year] += item["total_sales"]

  max_year = max(years, key=years.get)

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(
      format_car(max_sales["car"]), max_sales["total_sales"]),
    "The most popular year was {} with {} sales.".format(
      max_year, years[max_year])
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  print(summary)
  sender = "automation@example.com"
  recipient = "student-02-4131aa03c5f8@example.com"
  subject = "Sales summary for last month"
  body = "<br/>".join(summary)
  attachment_path = "/tmp/cars.pdf"

  # TODO: turn this into a PDF report
  reports.generate(attachment_path, subject, body, cars_dict_to_table(data))

  # TODO: send the PDF report as an email attachment
  body = "\n".join(summary)
  message = emails.generate(sender, recipient, subject, body, attachment_path)
  emails.send(message)


if __name__ == "__main__":
  main(sys.argv)
