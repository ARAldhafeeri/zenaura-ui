from public.components.common import *
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from public.loading import DOMIsReady
from public.styles import main_content, with_theme_colors_text_no_hover
class IntroSection(Component):
	def __init__(self):
		self.loading = True
		self.header_class =  "text-center max-w-[950px] pt-11 text-3xl font-bold text-light-gray1 dark:text-dark-page1"
		self.paragraph_class = "max-w-[550px] text-center pt-5 text-lg text-light-gray1 dark:text-dark-page1 text-foreground"
		self.btn_one_class = """
													inline-flex items-center justify-center 
													whitespace-nowrap text-sm font-medium 
													transition-colors focus-visible:outline-none 
													focus-visible:ring-1 focus-visible:ring-ring 
													disabled:pointer-events-none disabled:opacity-50 
													text-primary-foreground shadow 
													h-9 px-4 py-2 rounded-[6px]
													m-1 bg-light-gray1 text-light-white
													hover:bg-light-green
													dark:text-dark-page1
													dark:bg-dark-black
													dark:hover:bg-dark-gray2
												"""
		self.btn_two_class = """
													inline-flex items-center justify-center whitespace-nowrap 
													text-sm font-medium transition-colors focus-visible:outline-none 
													focus-visible:ring-1 focus-visible:ring-ring 
													disabled:pointer-events-none disabled:opacity-50 
													border border-input bg-background shadow-sm
													h-9 px-4 py-2 rounded-[6px]
													m-1 bg-light-white text-light-gray1
													hover:text-light-green
													dark:text-dark-black
													dark:hover:bg-dark-gray2
													dark:bg-dark-gray1
												"""
		
		self.active = "1"

	@mutator
	async def attached(self):
		await DOMIsReady()
		self.loading = False

	@mutator
	async def handle_active_tab(self, event):
			self.active = event.target.name

	def render(self):
		return  Div(main_content, [
			Section([
				Div("flex flex-col items-center bg-light-white dark:bg-dark-gray1 ", [
					Header1("Build modern UI/UX faster with zenaura/ui", self.header_class),
					Paragraph("Zenaura/UI enables developers to build modern web applications more efficiently by utilizing styled components and leveraging Tailwind CSS.", self.paragraph_class)
				]),
				Div("flex justify-center ", [
					Button(self.btn_one_class, "Get Started"),
					Button(self.btn_two_class, "Components") 
				]),
				TabsComponent(
					[
						TabButton(
							"1", 
							"Login Form", 
							self.active, 
							"intro_section.handle_active_tab", 
							with_theme_colors_text_no_hover(
								f"px-4 py-2 transition-all duration-300"
								)
						),
						TabButton(
							"2", 
							"Dashboard", 
							self.active, 
							"intro_section.handle_active_tab", 
							with_theme_colors_text_no_hover(
								f"px-4 py-2 transition-all duration-300"
								)
						),
						TabButton(
							"3", 
							"Admin", 
							self.active, 
							"intro_section.handle_active_tab", 
							with_theme_colors_text_no_hover(
								f"px-4 py-2 transition-all duration-300"
								)
						),
					],
					[
						TabContent("1",  self.active, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam aliquam justo nec justo lacinia, vel ullamcorper nibh tincidunt."),
						TabContent("2",  self.active,  "Proin non velit ac purus malesuada venenatis sit amet eget lacus. Morbi quis purus id ipsum ultrices aliquet Morbi quis."),
						TabContent("3",  self.active, "Fusce hendrerit urna vel tortor luctus, nec tristique odio tincidunt. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.")
					]
				)
			], "") if not self.loading else Loader()
		
		])
		