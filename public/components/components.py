import asyncio
from public.loading import DOMIsReady
from public.components.common import *
from public.components.nav import *
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class, with_theme_colors_text_no_hover

class Components(Component):
  def __init__(self):
      self.loading = True
      self.active_comp = "menu"
      self.active_tab = "1"
      self.open_menu = False

  @mutator
  async def attached(self):
    self.loading = False

  @mutator
  async def set_active_comp(self, event):
     self.active_comp = event.target.name

  @mutator
  async def set_active_tab(self, event):
     self.active_tab = "2" if self.active_tab == "1" else "1"
     print(self.active_tab)

  @mutator
  async def toggle_dropdown(self, _):
     self.open_menu = not self.open_menu

  def render(self):
    
    return  Div("w-screen h-screen py-[60px]", [
     MicroFrontend("https://araldhafeeri.github.io/zenaura-ui-comp/", "") 
    ])