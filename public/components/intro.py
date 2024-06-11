from public.components.common import *
from zenaura.client.component import Component

class IntroSection(Component):

		def render(self):
				return Section([
						Div("", [
								Header1("The Python Library For Pythonistas! e32 !", "text-3xl font-bold underline" ),
								Header1("Building Modern Web User Interface", "text-3xl font-bold underline")
						]),
						Button("intro-btn-1", "Start Creating"),
						Button("intro-btn-2", "API Reference")
				], "intro")
		