import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import time
from datetime import datetime

# This code returns New Zealand Time (NZT) including daylight saving
# Winter time (NZST) is UTC+12H, Summer time (NZDT) is UTC+13H
# Changes happen first Sunday of April (NZST) and last Sunday of September (NZDT) at 01:00 UTC
# Ref. formulas : http://www.webexhibits.org/daylightsaving/i.html
#                 Since 1996, valid through 2099

def nztime():
    year = time.localtime()[0]                  #get current year
    HHApril   = time.mktime((year,4 ,(0+(int(5*year/4+4))%7),1,0,0,0,0,0)) 	    #Time of April change to NZST
    HHSeptember = time.mktime((year,9,(31-(int(5*year/4+1))%7),1,0,0,0,0,0)) 	#Time of September change to NZDT
    now=time.time()
    if now < HHApril :               		    # we are before first sunday of April
        nzt=time.localtime(now+(13*3600)) 		# CET:  UTC+13H
    elif now < HHSeptember :           		    # we are before last sunday of September
        nzt=time.localtime(now+(12*3600)) 		# CEST: UTC+12H
    else:                            			# we are after last sunday of September
        nzt=time.localtime(now+(13*3600)) 	    # CET:  UTC+13H
    return(nzt)


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def record_reading(temperature, humidity):
  app_tables.readings.add_row(Time=nztime(), Temperature=temperature, Humidity=humidity)

@anvil.server.callable
def get_data():
  return app_tables.readings.search()
