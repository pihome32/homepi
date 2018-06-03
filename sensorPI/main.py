#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to run your app via command line
Usage: app_cli.py param1 param2
Options:
-h --help                   Show this screen.
-v --version                Show the app version
"""
from __future__ import absolute_import
from optparse import OptionParser, OptionGroup
from src import mqtt
from src import influxdb
from src import mpl115a2
from src import bme680
from web import *
import time
import schedule
import configparser
import threading
import subprocess




def every_minute():
	mpl115a2.read()

	
def every_10minutes():
	bme680.read()

    #print("I'm working...")

def init():
    mqttThread = threading.Thread(target=mqtt.mqttListener, args=())
    mqttThread.start()
    mpl115a2.read()
    bme680.read()
    

def mainloop():
    print("main")
    #test.mqttSend("dsfasdf",34323323)
    #bme680.read()
	
def main():
    """Main entry point for script."""

    # Declarations of Option Parser : https://docs.python.org/2/library/optparse.html
    parser = OptionParser(version="1.0")
    group = OptionGroup(parser, "Specific Options", "Your application parameters")
    group.add_option("-v", "--view", help="Show this software version", action="store_true", dest="view", default=False)
    group.add_option("-n", "--name", dest="name", help="Set a name")
    group.add_option("-c", "--configfile", dest="configfile", help="Config file")
    parser.add_option_group(group)
    (options, args) = parser.parse_args()

    # You're actions
    if options.view:
        print ("What a great view")
        return True

    # You're actions
    if options.configfile:
        config = configparser.ConfigParser()
        config.read(options.configfile)
        influxdb.init(config['INFLUXDB']['HOST'],config['INFLUXDB']['PORT'],config['INFLUXDB']['DB'])


    init()

    schedule.every(60).seconds.do(every_minute)
    schedule.every(600).seconds.do(every_10minutes)
    #schedule.every().hour.do(job)
    #schedule.every().day.at("10:30").do(job)
    #schedule.every(5).to(10).minutes.do(job)
    #schedule.every().monday.do(job)
    #schedule.every().wednesday.at("13:15").do(job)
    #mq= test.mqttListener ()





    while True:
        schedule.run_pending()
        mainloop()
        time.sleep(1)



if __name__ == "__main__":
    main()