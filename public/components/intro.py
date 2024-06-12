from public.components.common import *
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from public.loading import DOMIsReady
class IntroSection(Component):
		def __init__(self):
			self.loading = True
		@mutator
		async def attached(self):
			await DOMIsReady()
			self.loading = False

		def render(self):
			return  Div("min-h-screen pt-16 relative ", [
				Section([
					Div("h-full", [
								Header1("The Python Library For Pythonistas! e32 !", "text-3xl font-bold underline" ),
								Header1("Building Modern Web User Interface", "text-3xl font-bold underline")
						]),
						Button("intro-btn-1", "Start Creating"),
						Button("intro-btn-2", "API Reference") 
					], "")  if not self.loading else Loader()
				])
		