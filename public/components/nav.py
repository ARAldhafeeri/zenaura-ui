from .common import *
from zenaura.client.tags.builder import Builder

def NavItemText(href, text, class_names, click=None):
  tag = Builder('a') \
    .with_attribute("class", class_names) \
    .with_attribute("href", href) \
    .with_text(text)
  if click:
    tag.with_attribute("py-click", click)
       
  return tag.build()

def NavItemIcon(href, img, class_names=""):
  return  Builder('a').with_attribute('href', href).with_attribute("class", class_names).with_child(img).build()

def SvgPath(linecap, linejoin, d):
        return  Builder('path') \
          .with_attribute('stroke-linecap', linecap) \
          .with_attribute('stroke-linejoin', linejoin) \
          .with_attribute('d', d) \
          .build()

def Svg(class_name, fill, viewBox, stroke, path, stroke_width=None):
        svg = Builder('svg') \
          .with_attribute('class', class_name) \
          .with_attributes(
                  fill=fill,
                  viewBox=viewBox,
                  stroke=stroke
          ).with_child(
                path
          )
        if stroke_width:
                svg.with_attribute('stroke-width', stroke_width)
        return svg.build()

def Span(class_name, text=None):
        span =  Builder('span').with_attribute('class', class_name)
        if text:
                span.with_text(text)
        return span.build()

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
                "Docs", 
                f"rounded-md {'bg-light-green' if active == 'docs' else 'hover:bg-light-green hover:text-white'} px-3 py-2 text-sm font-medium text-light-white",
                click="nav_bar_header.navigate_to_docs"
            ),
            NavItemText(
            "javascript:;", 
            "Components", 
            f"rounded-md {'bg-light-green' if active == 'components' else 'hover:bg-light-green hover:text-white'}  px-3 py-2 text-sm bg-red font-medium text-light-white",
            "nav_bar_header.navigate_to_components"
            ),
            NavItemText(
                "javascript:;", 
                "Themes", 
                f"rounded-md {'bg-light-green' if active == 'theme' else 'hover:bg-light-green hover:text-white'} px-3 py-2 text-sm font-medium text-light-white",
                "nav_bar_header.navigate_to_theme"

            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                f"rounded-md {'bg-light-green' if active == 'example' else 'hover:bg-light-green hover:text-white'}  px-3 py-2 text-sm font-medium text-light-white",
                "nav_bar_header.navigate_to_examples"
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
                "Docs", 
                f"rounded-md text-left {'bg-light-green' if active == 'docs' else 'hover:bg-light-green hover:text-white'}  px-3 py-2 text-sm font-medium text-light-white"
            ),
            NavItemText(
            "javascript:;", 
            "Components", 
            f"rounded-md text-left {'bg-light-green' if active == 'components' else 'hover:bg-light-green hover:text-white'}  px-3 py-2 text-sm font-medium text-light-white",
            ),
            NavItemText(
                "javascript:;", 
                "Themes", 
              f"rounded-md text-left {'bg-light-green' if active == 'theme' else 'hover:bg-light-green hover:text-white'}  px-3 py-2 text-sm font-medium text-light-white",
            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                f"rounded-md text-left {'bg-light-green' if active == 'examples' else 'hover:bg-light-green hover:text-white'}  px-3 py-2 text-sm font-medium text-light-white"
            ),
          ]
        )
      ]
    )

def NavBarLogo():
    return  Div(
    "flex flex-shrink-0 items-center",
        [
            Image("./public/logo.png", "Your Company", "32", "32", "h-8 w-auto")
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
               Image("./public/dark.png", "toggle theme", "15", "15") if is_dark else Image("./public/light.png", "toggle theme", "15", "15")
            ],
            "nav_bar_header.toggle_theme"
        )
      ]
  )