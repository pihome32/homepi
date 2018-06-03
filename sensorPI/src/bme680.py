from subprocess import check_output
from src import influxdb

def read():

	data= str(check_output(["./lib/bme680/bme680_read", '1', '1']))
	data =data.split(',')

	temp= data[0]
	temp=temp.split("'")
	gas= data[3]
	gas=gas.split("'")
	pressure = float(data[1]) / 10
	db_data= { "Temperature": temp[1],"Pressure": pressure,"Humidity": data[2],"Gas": gas[0]}

	influxdb.write('bme680',db_data)
