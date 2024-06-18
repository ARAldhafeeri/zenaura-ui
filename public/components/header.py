from public.components.common import *
from public.components.nav import *
from zenaura.client.component import Component, Reuseable
from zenaura.client.mutator import mutator

class Header(Component):
	def __init__(self, router, class_names_nav="fixed left-0 right-0 z-40 bg-light-gray1", class_names_container="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8", class_names_div="relative flex h-16 items-center justify-between"):
		self.class_names_nav = class_names_nav
		self.class_names_container = class_names_container
		self.class_names_div = class_names_div
		self.show_mobile = False
		self.router = router 
		self.title = ""

	def update_title(self):
		info, context = self.router.get_current_route()
		if info:
			(_, self.title, _, _) = info
		else: 
			title = ""

	@mutator
	async def toggle_mobile_menu(self, event):
		self.show_mobile = not self.show_mobile

	async def navigate_to_docs(self, event):
		await self.router.navigate("/docs")
		self.update_title()

	async def navigate_to_components(self, event):
		await self.router.navigate("/components")
		self.update_title()
		
	async def navigate_to_theme(self, event):
		await self.router.navigate("/theme")
		self.update_title()
	
	async def navigate_to_examples(self, event):
		await self.router.navigate("/examples")
		self.update_title()

	@mutator
	async def attached(self):
		self.update_title()



	def render(self):
		return Builder('nav').with_attribute('class', self.class_names_nav).with_child(
			Div(self.class_names_container, [
				Div(self.class_names_div, [
						Div(
							"absolute inset-y-0 left-0 flex items-center sm:hidden", 
							[MenuSmallScreenBtn(self.show_mobile)]
						),
						Div(
							"""
							flex flex-1 items-center justify-center 
							sm:items-stretch sm:justify-start
							""", 
							[NavBarLogo(), NavBarItems(self.title)]
						),
						NavBarRightContent()
				]), 
				ButtonWithAttrsChildren("", {}, [
					NavBarItemsMobile(self.show_mobile, self.title)
				],
				)
			])
		).build()
		