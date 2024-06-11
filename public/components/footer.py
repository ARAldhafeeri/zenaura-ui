from zenaura.client.tags.builder import Builder
from zenaura.client.component import Component

class Footer(Component):
		def render(self):
				return Builder("footer").with_text("Zenaura@2024").build()