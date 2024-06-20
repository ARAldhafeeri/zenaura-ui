import asyncio
from public.loading import DOMIsReady
from public.components.common import *
from public.components.nav import *
from public.components.sidebar import Sidebar
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from public.styles import main_content
class Components(Component):
  def __init__(self):
      self.loading = True

  @mutator
  async def attached(self):
    await DOMIsReady()
    self.loading = False

  # feature reset 
  async def on_seatled(self):
    self.loading = True 

  def render(self):
    return  Div(main_content, [
      # main content
      Div("flex w-auto p-4 ", [
        	Section([
            Sidebar("test"),
						 Paragraph("""Lorem ipsum dolor sit amet consectetur, adipisicing elit. Expedita quam odit officiis
            magni doloribus ipsa dolore, dolores nihil accusantium labore, incidunt autem iure quae vitae voluptate,
            esse asperiores aliquam repellat. Harum aliquid non officiis porro at cumque eaque inventore iure. Modi sunt
            optio mollitia repellat sed ab quibusdam quos harum!"""),
					], "grid grid-cols-[20%_80%]") if not self.loading else Loader()
      ]) 
    ])