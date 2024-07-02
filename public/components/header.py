from public.components.common import *
from public.components.nav import *
from zenaura.client.component import Component, Reuseable
from zenaura.client.mutator import mutator
try:
	from pyscript import document
	from js import localStorage, sendMessageToIframes
except ImportError:
	# build server
	document = None 
	localStorage = None 
	sendMessageToIframes = None


class Header(Component):
	def __init__(self, router):
		self.class_names_nav = "fixed left-0 right-0 z-40 bg-light-gray1 dark:bg-dark-black"
		self.class_names_container = "mx-auto max-w-7xl px-2 sm:px-6 lg:px-8"
		self.class_names_div =  "relative flex h-16 items-center justify-between"
		self.show_mobile = False
		self.router = router 
		self.title = ""
		self.light = False 

	def update_title(self):
		info, context = self.router.get_current_route()
		if info:
			(_, self.title, _, _) = info
		else: 
			title = ""

	def theme_condition(self, condition):
		document.documentElement.classList.remove('dark') if condition else document.documentElement.classList.add('dark')
		localStorage.setItem("theme", "light") if condition else localStorage.setItem("theme", "dark")
		sendMessageToIframes('light-theme') if condition else sendMessageToIframes("dark-theme")
		self.light = condition

	@mutator
	async def toggle_mobile_menu(self, _):
		self.show_mobile = not self.show_mobile

	@mutator
	async def toggle_theme(self, _):
		self.light = not self.light
		self.theme_condition(self.light)
		


	async def navigate_to_docs(self, _):
		await self.router.navigate("/docs")
		self.update_title()

	async def navigate_to_components(self, _):
		await self.router.navigate("/components")
		self.update_title()
		
	async def navigate_to_theme(self, _):
		await self.router.navigate("/theme")
		self.update_title()
	
	async def navigate_to_examples(self, _):
		await self.router.navigate("/examples")
		self.update_title()

	@mutator
	async def attached(self):
		self.update_title()
		is_light = localStorage.getItem("theme") == "light"
		self.theme_condition(is_light)


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
						NavBarRightContent(self.light)
				]), 
				ButtonWithAttrsChildren("", {}, [
					NavBarItemsMobile(self.show_mobile, self.title)
				],
				)
			])
		).build()
		