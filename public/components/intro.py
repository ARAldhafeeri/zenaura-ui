from public.components.common import *
from zenaura.client.component import Component
from zenaura.client.mutator import mutator
from public.loading import DOMIsReady
from public.components.tabs import TabsComponent, TabContent, TabButton
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
													"""
		@mutator
		async def attached(self):
			await DOMIsReady()
			self.loading = False

		def render(self):
			return  Div("min-h-screen  pt-16 relative bg-light-white dark:bg-dark-gray1 mx-auto flex max-w-[980px] flex-col items-center gap-2 py-8 md:py-12 md:pb-8 lg:py-24 lg:pb-20 ", [
					Section([
						Div("h-full bg-light-white dark:bg-dark-gray1 ", [
									Header1("Build modern UI/UX faster with zenaura/ui", self.header_class),
									Paragraph("Zenaura/UI enables developers to build modern web applications more efficiently by utilizing styled components and leveraging Tailwind CSS.", self.paragraph_class)
							]),
							Div("flex justify-center ", [
								Button(self.btn_one_class, "Get Started"),
								Button(self.btn_two_class, "Components") 
							]),
						TabsComponent(
							[
								TabButton(1, "Section 1", "openTab"),
								TabButton(2, "Section 2",  "openTab"),
								TabButton(3, "Section 3",  "openTab")
							],
							[
								TabContent(1,  "openTab", "Section 1 Content", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam aliquam justo nec justo lacinia, vel ullamcorper nibh tincidunt."),
								TabContent(2,  "openTab", "Section 2 Content", "Proin non velit ac purus malesuada venenatis sit amet eget lacus. Morbi quis purus id ipsum ultrices aliquet Morbi quis."),
								TabContent(3,  "openTab", "Section 3 Content", "Fusce hendrerit urna vel tortor luctus, nec tristique odio tincidunt. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.")
							]
						)
					], "") if not self.loading else Loader()
				
				])
		