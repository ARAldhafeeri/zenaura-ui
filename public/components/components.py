import asyncio
from public.loading import DOMIsReady
from public.components.common import *
from public.components.nav import *
from public.components.sidebar import Sidebar
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class, with_theme_colors_text_no_hover
from public.styled.menu import MenuExample
from public.constants import menu_component_code

def StyledComponents(active_comp, active_tab, context):
  return Div("p-10", 
    [
      StyledComponentPresentation(
         "Menu",
         "Display a menu to the user - triggered by py-click",
         "url",
         MenuExample(context["open"]),
         menu_component_code,
         "menu",
         active_comp, 
         active_tab
      ),
      StyledComponentPresentation(
         "Breadcrumb",
         "Display hierarchical path to the current resurces - helps users identify their current location within web app. ",
         "url",
         Button(btn_one_class, "open", "null", "menu"),
         menu_component_code,
         "breadcrumb",
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
      self.open_menu = False

  @mutator
  async def attached(self):
    await DOMIsReady()
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
    
    return  Div(main_content, [
      # main content
      Section([
        Sidebar(),
        StyledComponents(self.active_comp, self.active_tab, {"open": self.open_menu})
      ], "grid grid-cols-[20%_80%]") if not self.loading else Loader()
    ])