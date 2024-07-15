from ._anvil_designer import HumidityTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go

class Humidity(HumidityTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def timer_2t_hum(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    data = anvil.server.call_s('get_data')

    #self.temp_plot.data = go.Scatter(x = [r['Time'] for r in data], y = [r['Temperature'] for r in data], fill = 'tozeroy')
    self.hum_plot.data = go.Scatter(x = [r['Time'] for r in data], y = [r['Humidity'] for r in data], fill = 'tozeroy')