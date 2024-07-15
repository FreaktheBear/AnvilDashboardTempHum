import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import time
from datetime import datetime
#
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def record_reading(temperature, humidity):
  app_tables.readings.add_row(Temperature=temperature, Humidity=humidity, Time=datetime.now())

@anvil.server.callable
def get_data():
  return app_tables.readings.search()
