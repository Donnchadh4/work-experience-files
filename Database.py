#!/usr/bin/python

import MySQLdb

#Open database connection
db = MySQLdb.connect("maindb-read-rep-1.cvq5x16iz667.eu-west-1.rds.amazonaws.com","admin","mvemj6u9p","number_tester")

#prepare a crusor object using cursor() method
cursor = db.cursor()

#execute SQL query using execute() method
cursor.execute("select p.name, jp.country_code_id, count(jp.id), sum(if(unix_timestamp(jp.end_call_processing_timestamp), unix_timestamp(jp.end_call_processing_timestamp) - unix_timestamp(jp.start_call_processing_timestamp), 0)) as duration from job_processing as jp left join providers as p on (p.id = jp.provider_id) where year(start_call_processing_timestamp) = 2014 and month(jp.start_call_processing_timestamp)=5 and jp.id > 1000000 group by p.name, jp.country_code_id;")

#----------------------------------------------------------------------------------
import csv

def csvWriter(data,path):
	"""write data from database to a csv file"""
	with open(path,"wb") as csv_f:
		writer = csv.writer(csv_f,delimiter=',')
		for line in data:
			writer.writerow(line)
#---------------------------------------------------------------
if __name__ == "__main__":
	
	records = ["Provider,Country,Amount,Duration".split(",")]
	for record in cursor.fetchall():
		records.append(record)
	path = "Spearline.csv"
	csvWriter(records,path)


#disconnect from server
db.close()
