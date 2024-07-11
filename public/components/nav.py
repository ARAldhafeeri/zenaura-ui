from .common import *
from zenaura.client.tags.builder import Builder
from public.styles import with_theme_colors

def MenuSmallScreenBtn(show=False):
  xShow = "block" if show else "hidden"
  menuShow = "hidden" if show else "block"
  return ButtonWithAttrsChildren(
    class_name="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-light-green hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white",
    attrs={"type" : "button", "py-click": "nav_bar_header.toggle_mobile_menu"}, 
    children=[
      Span(class_name="absolute -inset-0.5"),
      Span(class_name="sr-only", text="Open main menu"),
      Svg(
        class_name=f"{menuShow} h-6 w-6", 
        fill="none", 
        viewBox="0 0 24 24", 
        stroke="currentColor", 
        path=SvgPath(
                linecap="round", 
                linejoin="round", 
                d='M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5'
        )
      ), 
      Svg(
        class_name=f"{xShow} h-6 w-6", 
        fill="none", 
        viewBox="0 0 24 24", 
        stroke="currentColor", 
        path=SvgPath(
                linecap="round", 
                linejoin="round", 
                d='M6 18L18 6M6 6l12 12'
        ),
        stroke_width="1.5"
      )
    ]
  )

active_item_class = "text-light-green dark:text-dark-gray1"
inactive_item_class = with_theme_colors("")

def NavBarItems(active):
    return Div(
      "hidden sm:ml-6 sm:block",
      [
        Div(
          "flex space-x-4", 
          # add more nav items here
          [
            NavItemText(
            "javascript:;", 
            "Components", 
            f"rounded-md {active_item_class if active == 'components' else inactive_item_class}  px-3 py-2 text-sm bg-red font-medium text-light-white",
            "nav_bar_header.navigate_to_components"
            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                f"rounded-md {active_item_class if active == 'example' else inactive_item_class}  px-3 py-2 text-sm font-medium text-light-white",
                "nav_bar_header.navigate_to_examples"
            ),
            NavItemText(
                "javascript:;", 
                "Charts", 
                f"rounded-md text-left {active_item_class if active == 'charts' else inactive_item_class}  px-3 py-2 text-sm font-medium text-light-white",
                "nav_bar_header.navigate_to_charts"

            ),
          ]
        )
      ]
    )

def NavBarItemsMobile(show, active):
    visable = "" if show else "hidden"
    return Div(
      visable,
      [
        Div(
          "flex flex-col w-full space-y-1 px-2 pb-3 pt-2", 
          # add more nav items here
          [
            NavItemText(
            "javascript:;", 
            "Components", 
            f"rounded-md text-left {active_item_class if active == 'components' else inactive_item_class}  px-3 py-2 text-sm font-medium text-light-white",
            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                f"rounded-md text-left {active_item_class if active == 'examples' else inactive_item_class}  px-3 py-2 text-sm font-medium text-light-white"
            ),
            NavItemText(
                "javascript:;", 
                "Charts", 
                f"rounded-md text-left {active_item_class if active == 'charts' else inactive_item_class}  px-3 py-2 text-sm font-medium text-light-white"
            ),
          ]
        )
      ]
    )

def NavBarLogo():
    return  Div(
    "flex flex-shrink-0 items-center",
        [
            Image("./public/imgs/logo.png", "Your Company", "32", "32", "h-8 w-auto")
        ]
    )

def NavBarRightContent(is_dark):
    return Div(
    "absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0", 
      [
      
        ButtonWithAttrsChildren(
            "relative",
            {"type": "button"},
            [
                Span("absolute -inset-1.5"),
                Span("sr-only", "View notifications"),
               Image("./public/imgs/dark.png", "toggle theme", "15", "15") if is_dark else Image("./public/imgs/light.png", "toggle theme", "15", "15")
            ],
            "nav_bar_header.toggle_theme"
        )
      ]
  )

