import asyncio
from public.loading import DOMIsReady
from public.components.common import *
from public.components.nav import *
from public.components.sidebar import Sidebar
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class, with_theme_colors_text_no_hover
from public.constants import menu_component_code
def StyledComponents(active_comp, active_tab):
  return Div("p-10", 
    [
      StyledComponentPresentation(
         "Menu",
         "Display a menu to the user - triggered by py-click",
         "url",
         Button(btn_one_class, "open", "null", "menu"),
         menu_component_code,
         "menu",
         active_comp, 
         active_tab
      ),
      StyledComponentPresentation(
         "Menu",
         "Display a menu to the user - triggered by py-click",
         "url",
         Button(btn_one_class, "open", "null", "menu"),
         menu_component_code,
         "menu",
         active_comp, 
         active_tab
      ),
    ]
  )


class Components(Component):
  def __init__(self):
      self.loading = True
      self.active_comp = "menu"
      self.active_tab = "1"

  @mutator
  async def attached(self):
    await DOMIsReady()
    self.loading = False

  @mutator
  async def set_active_comp(self, event):
     self.active_comp = event.target.name

  @mutator
  async def set_active_tab(self, event):
     self.active_tab = "2" if self.active_tab == "1" else "2"

  def render(self):
    
    return  Div(main_content, [
      # main content
      Section([
        Sidebar(),
        StyledComponents(self.active_comp, self.active_tab)
      ], "grid grid-cols-[20%_80%]") if not self.loading else Loader()
    ])