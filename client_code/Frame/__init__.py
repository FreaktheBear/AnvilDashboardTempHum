from ._anvil_designer import FrameTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Humidity import Humidity
from ..Temperature import Temperature

#This is your startup form. It has a sidebar with navigation links and a content panel where page content will be added.
class Frame(FrameTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #Present users with a login form with just one line of code:
    anvil.users.login_with_form()

    #Set the Plotly plots template to match the theme of the app
    Plot.templates.default = "rally"
    #When the app starts up, the Temperature form will be added to the page
    self.content_panel.add_component(Temperature())
    #Change the color of the temp_page_link to indicate that the Temperature page has been selected
    self.temp_page_link.background = app.theme_colors['Primary Container']
    

  def temp_page_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    #Clear the content panel and add the Temperature Form
    self.content_panel.clear()
    self.content_panel.add_component(Temperature())
    #Change the color of the temp_page_link to indicate that the Temperature page has been selected
    self.temp_page_link.background = app.theme_colors['Primary Container']
    self.hum_page_link.background = "transparent"

  def hum_page_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    #Clear the content panel and add the Humidity Form
    self.content_panel.clear()
    self.content_panel.add_component(Humidity())
    #Change the color of the hum_page_link to indicate that the Humidity page has been selected
    self.hum_page_link.background = app.theme_colors['Primary Container']
    self.temp_page_link.background = "transparent"

  #If using the Users service, uncomment this code to log out the user:
  def signout_link_click(self, **event_args):
  #   """This method is called when the link is clicked"""
    anvil.users.logout()
    open_form('Logout')








