from .common import *
from zenaura.client.tags.builder import Builder
from public.styles import with_theme_colors
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

active_item_class = 'bg-light-green dark:bg-dark-gray2 text-light-white dark:text-dark-page1'
inactive_item_class = with_theme_colors("px-3 py-2 text-sm")
category_class_name = with_theme_colors("mb-1 rounded-md px-2 py-1 text-sm font-semibold")
def Sidebar(active):
    return Div(
          "flex flex-col space-y-2 h-screen p-2 overflow-y-scroll", 
          # add more nav items here
          [
            # category1
            Header1("category1", category_class_name),
            NavItemText(
                "javascript:;", 
                "Docs", 
                f"rounded-md {active_item_class if active == 'docs' else inactive_item_class} ",
                click="nav_bar_header.navigate_to_docs"
            ),
            NavItemText(
            "javascript:;", 
            "Components", 
            f"rounded-md {active_item_class if active == 'components' else inactive_item_class}  ",
            "nav_bar_header.navigate_to_components"
            ),
            NavItemText(
                "javascript:;", 
                "Themes", 
                f"rounded-md {active_item_class if active == 'theme' else inactive_item_class} ",
                "nav_bar_header.navigate_to_theme"

            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                f"rounded-md {active_item_class if active == 'example' else inactive_item_class}  ",
                "nav_bar_header.navigate_to_examples"
            ),
            # category 2
            Header1("category2", category_class_name),
            NavItemText(
                "javascript:;", 
                "Docs", 
                f"rounded-md {active_item_class if active == 'docs' else inactive_item_class} ",
                click="nav_bar_header.navigate_to_docs"
            ),
            NavItemText(
            "javascript:;", 
            "Components", 
            f"rounded-md {active_item_class if active == 'components' else inactive_item_class}  ",
            "nav_bar_header.navigate_to_components"
            ),
            NavItemText(
                "javascript:;", 
                "Themes", 
                f"rounded-md {active_item_class if active == 'theme' else inactive_item_class} ",
                "nav_bar_header.navigate_to_theme"

            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                f"rounded-md {active_item_class if active == 'example' else inactive_item_class}  ",
                "nav_bar_header.navigate_to_examples"
            ),

            # category 2
            Header1("category2", category_class_name),
            NavItemText(
                "javascript:;", 
                "Docs", 
                f"rounded-md {active_item_class if active == 'docs' else inactive_item_class} ",
                click="nav_bar_header.navigate_to_docs"
            ),
            NavItemText(
            "javascript:;", 
            "Components", 
            f"rounded-md {active_item_class if active == 'components' else inactive_item_class}  ",
            "nav_bar_header.navigate_to_components"
            ),
            NavItemText(
                "javascript:;", 
                "Themes", 
                f"rounded-md {active_item_class if active == 'theme' else inactive_item_class} ",
                "nav_bar_header.navigate_to_theme"

            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                f"rounded-md {active_item_class if active == 'example' else inactive_item_class}  ",
                "nav_bar_header.navigate_to_examples"
            ),

            # category 2
            Header1("category2", category_class_name),
            NavItemText(
                "javascript:;", 
                "Docs", 
                f"rounded-md {active_item_class if active == 'docs' else inactive_item_class} ",
                click="nav_bar_header.navigate_to_docs"
            ),
            NavItemText(
            "javascript:;", 
            "Components", 
            f"rounded-md {active_item_class if active == 'components' else inactive_item_class}  ",
            "nav_bar_header.navigate_to_components"
            ),
            NavItemText(
                "javascript:;", 
                "Themes", 
                f"rounded-md {active_item_class if active == 'theme' else inactive_item_class} ",
                "nav_bar_header.navigate_to_theme"

            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                f"rounded-md {active_item_class if active == 'example' else inactive_item_class}  ",
                "nav_bar_header.navigate_to_examples"
            ),

                  # category 2
            Header1("category2", category_class_name),
            NavItemText(
                "javascript:;", 
                "Docs", 
                f"rounded-md {active_item_class if active == 'docs' else inactive_item_class} ",
                click="nav_bar_header.navigate_to_docs"
            ),
            NavItemText(
            "javascript:;", 
            "Components", 
            f"rounded-md {active_item_class if active == 'components' else inactive_item_class}  ",
            "nav_bar_header.navigate_to_components"
            ),
            NavItemText(
                "javascript:;", 
                "Themes", 
                f"rounded-md {active_item_class if active == 'theme' else inactive_item_class} ",
                "nav_bar_header.navigate_to_theme"

            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                f"rounded-md {active_item_class if active == 'example' else inactive_item_class}  ",
                "nav_bar_header.navigate_to_examples"
            ),

                         # category 2
            Header1("category2", category_class_name),
            NavItemText(
                "javascript:;", 
                "Docs", 
                f"rounded-md {active_item_class if active == 'docs' else inactive_item_class} ",
                click="nav_bar_header.navigate_to_docs"
            ),
            NavItemText(
            "javascript:;", 
            "Components", 
            f"rounded-md {active_item_class if active == 'components' else inactive_item_class}  ",
            "nav_bar_header.navigate_to_components"
            ),
            NavItemText(
                "javascript:;", 
                "Themes", 
                f"rounded-md {active_item_class if active == 'theme' else inactive_item_class} ",
                "nav_bar_header.navigate_to_theme"

            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                f"rounded-md {active_item_class if active == 'example' else inactive_item_class}  ",
                "nav_bar_header.navigate_to_examples"
            ),

                         # category 2
            Header1("category2", category_class_name),
            NavItemText(
                "javascript:;", 
                "Docs", 
                f"rounded-md {active_item_class if active == 'docs' else inactive_item_class} ",
                click="nav_bar_header.navigate_to_docs"
            ),
            NavItemText(
            "javascript:;", 
            "Components", 
            f"rounded-md {active_item_class if active == 'components' else inactive_item_class}  ",
            "nav_bar_header.navigate_to_components"
            ),
            NavItemText(
                "javascript:;", 
                "Themes", 
                f"rounded-md {active_item_class if active == 'theme' else inactive_item_class} ",
                "nav_bar_header.navigate_to_theme"

            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                f"rounded-md {active_item_class if active == 'example' else inactive_item_class}  ",
                "nav_bar_header.navigate_to_examples"
            ),
          ]
        )


