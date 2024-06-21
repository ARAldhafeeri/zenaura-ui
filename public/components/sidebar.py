from .common import *
from zenaura.client.tags.builder import Builder
from public.styles import with_theme_colors, with_theme_colors_text_no_hover
def NavItemText(href, text, class_names, click=None):
  tag = Builder('a') \
    .with_attribute("class", class_names) \
    .with_attribute("href", href) \
    .with_text(text)
  if click:
    tag.with_attribute("py-click", click)
       
  return tag.build()


def Span(class_name, text=None):
        span =  Builder('span').with_attribute('class', class_name)
        if text:
                span.with_text(text)
        return span.build()

nav_item_style = with_theme_colors("px-3 py-2 text-sm")
category_class_name = with_theme_colors_text_no_hover("mb-1 rounded-md px-2 py-1 text-md font-semibold")

def SideBarNavigation():
	return [
		Header1("Navigation", category_class_name),
		NavItemText(
				"javascript:;", 
				"Menu", 
				nav_item_style,
				click="nav_bar_header.navigate_to_docs"
		),
		NavItemText(
		"javascript:;", 
		"Breadcrumb", 
		nav_item_style,
		"nav_bar_header.navigate_to_components"
		),
		NavItemText(
				"javascript:;", 
				"Dropdown", 
				nav_item_style,
				"nav_bar_header.navigate_to_theme"

		),
		NavItemText(
		"javascript:;", 
		"Steps", 
		nav_item_style,
		"nav_bar_header.navigate_to_examples"
		),
		NavItemText(
				"javascript:;", 
				"Steps", 
				nav_item_style,
				"nav_bar_header.navigate_to_examples"
		),
	]

def SideBarDataEntry():
	return [
		# Data Entry
		Header1("Data Entry", category_class_name),
		NavItemText(
      "javascript:;", 
      "Button", 
      nav_item_style,
      click="nav_bar_header.navigate_to_docs"
		),
		NavItemText(
      "javascript:;", 
      "Input", 
      nav_item_style,
      "nav_bar_header.navigate_to_components"
		),
		NavItemText(
      "javascript:;", 
      "InputNumber", 
      nav_item_style,
      "nav_bar_header.navigate_to_theme"
		),
		NavItemText(
      "javascript:;", 
      "Checkbox", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Radio", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Select", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Switch", 
      nav_item_style,
      click="nav_bar_header.navigate_to_docs"
		),
		NavItemText(
      "javascript:;", 
      "Slider", 
      nav_item_style,
      "nav_bar_header.navigate_to_components"
		),
		NavItemText(
      "javascript:;", 
      "DatePicker", 
      nav_item_style,
      "nav_bar_header.navigate_to_theme"

		),
		NavItemText(
      "javascript:;", 
      "TimePicker", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Upload", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Form", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
	]

def SideBarDataDisplay():
	return [
		Header1("Data Display", category_class_name),
		NavItemText(
      "javascript:;", 
      "Avatar", 
      nav_item_style,
      click="nav_bar_header.navigate_to_docs"
		),
		NavItemText(
      "javascript:;", 
      "Badge", 
      nav_item_style,
      "nav_bar_header.navigate_to_components"
		),
		NavItemText(
      "javascript:;", 
      "Card", 
      nav_item_style,
      "nav_bar_header.navigate_to_theme"
		),
		NavItemText(
      "javascript:;", 
      "Carousel", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Collapse", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Popover", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Tag", 
      nav_item_style,
      click="nav_bar_header.navigate_to_docs"
		),
		NavItemText(
      "javascript:;", 
      "Slider", 
      nav_item_style,
      "nav_bar_header.navigate_to_components"
		),
		NavItemText(
      "javascript:;", 
      "Table", 
      nav_item_style,
      "nav_bar_header.navigate_to_theme"

		),
		NavItemText(
      "javascript:;", 
      "Tree", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Tabs", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
	]

def SideBarFeedBack():
  return [
    Header1("Feedback", category_class_name),
		NavItemText(
      "javascript:;", 
      "Modal", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Message", 
      nav_item_style,
      click="nav_bar_header.navigate_to_docs"
		),
		NavItemText(
      "javascript:;", 
      "Notification", 
      nav_item_style,
      "nav_bar_header.navigate_to_components"
		),
		NavItemText(
      "javascript:;", 
      "Progress", 
      nav_item_style,
      "nav_bar_header.navigate_to_theme"

		),
		NavItemText(
      "javascript:;", 
      "Spin", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Skeleton", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),      
  ]

def SideBarOthers():
  return [
  Header1("Others", category_class_name),
		NavItemText(
      "javascript:;", 
      "Affix", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Anchor", 
      nav_item_style,
      click="nav_bar_header.navigate_to_docs"
		),
		NavItemText(
      "javascript:;", 
      "BackTop", 
      nav_item_style,
      "nav_bar_header.navigate_to_components"
		),
		NavItemText(
      "javascript:;", 
      "Divider", 
      nav_item_style,
      "nav_bar_header.navigate_to_theme"

		),
		NavItemText(
      "javascript:;", 
      "Drawer", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Image", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),   
		NavItemText(
      "javascript:;", 
      "List", 
      nav_item_style,
      "nav_bar_header.navigate_to_theme"

		),
		NavItemText(
      "javascript:;", 
      "Mention", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),
		NavItemText(
      "javascript:;", 
      "Rate", 
      nav_item_style,
      "nav_bar_header.navigate_to_examples"
		),   
  ]

def Sidebar(active):
	return Div(
		"flex flex-col space-y-2 h-screen p-2 overflow-y-scroll", 
		# add more nav items here
		[
			# Navigation
			*SideBarNavigation(),
      *SideBarDataEntry(),
			*SideBarDataDisplay(),
      *SideBarFeedBack(),
      *SideBarOthers()
		]
	)


