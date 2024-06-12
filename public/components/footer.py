from zenaura.client.tags.builder import Builder
from zenaura.client.component import Component

class Footer(Component):
		def render(self):
				return Builder("div").with_attribute("class", "fixed inset-x-0 bottom-0").with_child(Builder("div").with_text("Zenaura@2024").build()).build()