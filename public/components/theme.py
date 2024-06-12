import asyncio
from public.loading import DOMIsReady
from public.components.common import *
from public.components.nav import *
from zenaura.client.component import Component
from zenaura.client.mutator import mutator


class Theme(Component):
  def __init__(self):
    self.loading = True

  @mutator
  async def attached(self):
    await DOMIsReady()
    # just wait for better ui/ux
    await asyncio.sleep(0.3)
    self.loading = False
  
  def render(self):
    return  Div("min-h-screen pt-16 relative ", [
      Header1("theme","pt-16") if not self.loading else Loader()
    ])