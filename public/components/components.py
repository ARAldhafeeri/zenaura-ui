import asyncio
from public.loading import DOMIsReady
from public.components.common import *
from public.components.nav import *
from public.components.sidebar import Sidebar
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from public.styles import main_content, btn_one_class, with_theme_colors_text_no_hover
from public.components.tabs import TabContent, TabButton, TabsComponent


# passed to StyledComponentPresentation
# (header, paragraph, api_ref, preview_and_code, name, active)
content = [
  lambda active : ( 
    "Menu",
    "Display a menu of options to the user - triggered by a button click", 
    Button(btn_one_class, "API Refrence"),
    TabsComponent(
      [
        TabButton(
          "1", 
          "Login Form", 
          active, 
          "intro_section.handle_active_tab", 
          with_theme_colors_text_no_hover(
            f"px-4 py-2 transition-all duration-300"
            )
        ),
        TabButton(
          "2", 
          "Dashboard", 
          active, 
          "intro_section.handle_active_tab", 
          with_theme_colors_text_no_hover(
            f"px-4 py-2 transition-all duration-300"
            )
        ),
        TabButton(
          "3", 
          "Admin", 
          active, 
          "intro_section.handle_active_tab", 
          with_theme_colors_text_no_hover(
            f"px-4 py-2 transition-all duration-300"
            )
        ),
      ],
      [
        TabContent("1",  active, "Section 1 Content", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam aliquam justo nec justo lacinia, vel ullamcorper nibh tincidunt."),
        TabContent("2",  active, "Section 2 Content", "Proin non velit ac purus malesuada venenatis sit amet eget lacus. Morbi quis purus id ipsum ultrices aliquet Morbi quis."),
      ]
    )
  )
]
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
  async def set_active_comp(self, event):
     self.active_comp = event.target.name

  def render(self):
    return  Div(main_content, [
      # main content
      Div("flex w-auto p-4 ", [
        	Section([
            Sidebar("test"),
            Div("p-10", [
              Paragraph("""Lorem ipsum dolor sit amet consectetur, adipisicing elit. Expedita quam odit officiis
              magni doloribus ipsa dolore, dolores nihil accusantium labore, incidunt autem iure quae vitae voluptate,
              esse asperiores aliquam repellat. Harum aliquid non officiis porro at cumque eaque inventore iure. Modi sunt
              optio mollitia repellat sed ab quibusdam quos harum!"""),
                Paragraph("""Lorem ipsum dolor sit amet consectetur, adipisicing elit. Expedita quam odit officiis
              magni doloribus ipsa dolore, dolores nihil accusantium labore, incidunt autem iure quae vitae voluptate,
              esse asperiores aliquam repellat. Harum aliquid non officiis porro at cumque eaque inventore iure. Modi sunt
              optio mollitia repellat sed ab quibusdam quos harum!"""),
            ])
					], "grid grid-cols-[20%_80%]") if not self.loading else Loader()
      ]) 
    ])