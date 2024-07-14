from ._anvil_designer import TemperatureTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Temperature(TemperatureTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    data = anvil.server.call_s('get_data')

    self.temp_plot.data = go.Scatter(x = [r['Time'] for r in data], y = [r['Temperature'] for r in data], fill = 'tozeroy')
    self.hum_plot.data = go.Scatter(x = [r['Time'] for r in data], y = [r['Humidity'] for r in data], fill = 'tozeroy')

    

