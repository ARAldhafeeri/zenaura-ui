import asyncio
from public.components.common import *
from public.components.nav import *
from zenaura.client.component import Component
from zenaura.client.mutator import mutator

class Charts(Component):
  def render(self):
    return  Div("w-screen h-screen py-[60px]", [
     MicroFrontend("https://araldhafeeri.github.io/zenaura-ui-charts/", "") 
    ])