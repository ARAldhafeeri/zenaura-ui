from zenaura.client.tags.builder import Builder
from zenaura.client.component import Component

class Footer(Component):
		def render(self):
				return Builder("div").with_attribute("class", "fixed bottom-0 flex items-center justify-center left-0 right-0 z-40 px-4 py-3  text-white bg-gray-800 ").with_child(Builder("div").with_text("Zenaura@2024").build()).build()