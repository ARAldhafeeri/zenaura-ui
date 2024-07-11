from public.components.common import *
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from zenaura.ui.charts import ChartThis
from public.loading import DOMIsReady
from public.styles import main_content, with_theme_colors_text_no_hover
from .fin_tech import fintech_layout
from .ecommerce import ecommerce_layout
from .social_media_feed import social_media_layout
try : 
	from pyscript import window
except ImportError:
	fintechDashPanel = None
	window = None

config  = {
    "type": 'line',
    "data": {
        "labels": ['3 Apr', '4 Apr', '5 Apr', '6 Apr', '7 Apr', '8 Apr'],
        "datasets": [
            {
                "label": 'Income',
                "data": [500, 178, 450, 380, 610, 900],
                "backgroundColor": 'rgba(54, 162, 235, 0.2)',
                "borderColor": 'rgba(54, 162, 235, 1)',
                "borderWidth": 1,
                "fill": True,
            },
            {
                "label": 'Expenses',
                "data": [700, 623, 350, 580, 420, 700],
                "backgroundColor": 'rgba(255, 99, 132, 0.2)',
                "borderColor": 'rgba(255, 99, 132, 1)',
                "borderWidth": 1,
                "fill": True,
            },
        ],
    },
    "options": {
        "responsive": True,
        "scales": {
            "y": {
                "beginAtZero": True,
            },
        },
        "interaction": {
            "mode": 'index',
            "intersect": False,
        },
    }
}


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
		ChartThis(config, "panel")

	@mutator
	async def handle_active_tab(self, event):
			self.active = event.target.name
			
	def go_to_docs(self, _):
		window.open("https://araldhafeeri.github.io/Zenaura/zenaura-ui/installation/", "_blank")

	def go_to_api(self, _):
		window.open("https://araldhafeeri.github.io/Zenaura/api/ui/badge/#zenaura.ui.badge.Badge", "_blank")

	def render(self):
		return  Div(main_content, [
			Section([
				Div("flex flex-col items-center bg-light-white dark:bg-dark-gray1 ", [
					Header1("Build modern UI/UX faster with zenaura/ui", self.header_class),
					Paragraph("Zenaura/UI enables developers to build modern web applications more efficiently by utilizing styled components and leveraging Tailwind CSS.", self.paragraph_class)
				]),
				Div("flex justify-center ", [
					Button(self.btn_one_class, "Get Started", "intro_section.go_to_docs" ),
					Button(self.btn_two_class, "Components APIs",  "intro_section.go_to_api") 
				]),
				TabsComponent(
					[
						TabButton(
							"1", 
							"Fintech dashboard", 
							self.active, 
							"intro_section.handle_active_tab", 
							with_theme_colors_text_no_hover(
								f"px-4 py-2 transition-all duration-300"
								)
						),
						TabButton(
							"2", 
							"Ecomerace", 
							self.active, 
							"intro_section.handle_active_tab", 
							with_theme_colors_text_no_hover(
								f"px-4 py-2 transition-all duration-300"
								)
						),
						TabButton(
							"3", 
							"Social Media feed", 
							self.active, 
							"intro_section.handle_active_tab", 
							with_theme_colors_text_no_hover(
								f"px-4 py-2 transition-all duration-300"
								)
						)
					],
					[
						TabContent("1",  self.active, fintech_layout),
						TabContent("2",  self.active, ecommerce_layout),
						TabContent("3",  self.active, social_media_layout)					]
				)
			], "") 
		
		])
		