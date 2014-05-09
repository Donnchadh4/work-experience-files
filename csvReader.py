#!/usr/bin/env python

import csv

def csv_Dict_reader(file_obj):
	"""
	read a CSV file using csv.DictReader
	"""
	reader = csv.DictReader(file_obj, delimiter=',')
	for line in reader:
		print(line["Zimbabwe"])

#--------------------------
if __name__ == "__main__":
	with open("TB_notifications_2014-05-07.csv") as f_obj:
		csv_Dict_reader(f_obj)
